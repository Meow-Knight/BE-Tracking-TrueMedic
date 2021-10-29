from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api_information.models import Shipment, Agent, Producer
from api_information.serializers import ShipmentSerializer

import requests
from datetime import datetime


class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer

    @action(methods=["get"], detail=False)
    def tracking(self, request, *args, **kwargs):
        shipment_id = request.query_params.get("shipment")
        if not shipment_id:
            return Response(
                {"details": "shipment not found on url"},
                status=status.HTTP_400_BAD_REQUEST
            )

        producers = list(Producer.objects.all())
        agents = list(Agent.objects.all())

        factors = producers + agents

        transactions = {}

        self.get_transactions(transactions, shipment_id, producers)
        self.get_transactions(transactions, shipment_id, agents)

        transactions = self.get_valid_transactions(transactions, factors)
        sorted_transactions = sorted(transactions.items())
        for transaction in sorted_transactions:
            value = transaction[1]
            from_address = value.get('from')
            to_address = value.get('to')

            from_object = next(filter(lambda x: x.eth_address.lower() == from_address, factors), None)
            to_object = next(filter(lambda x: x.eth_address.lower() == to_address, factors), None)

            value['from_name'] = from_object.name
            value['to_name'] = to_object.name
            value['time'] = datetime.utcfromtimestamp(int(transaction[0])).strftime('%Y-%m-%d %H:%M:%S')

        result = map(lambda item: item[1], sorted_transactions)
        return Response(
            result,
            status=status.HTTP_200_OK
        )

    def get_transactions(self, transactions, shipment_id, accounts):
        for account in accounts:
            response = requests.get("https://api-ropsten.etherscan.io/api",
                                    params={
                                        "module": "account",
                                        "action": "txlist",
                                        "address": account.eth_address,
                                        "tag": "latest",
                                        "apikey": "H8636QMIEB5JDH1DMKJSVS8B54XJP2KSQU",
                                    },
                                    headers={
                                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, '
                                                      'like Gecko) Chrome/50.0.2661.102 Safari/537.36'})
            res_status = response.json().get("status")
            print(response.json())
            if res_status == '1':
                result = response.json().get("result")
                for e in result:
                    decoded_input = bytes.fromhex(e.get('input')[2:]).decode('ascii', 'ignore')
                    if shipment_id in decoded_input:
                        transactions[e.get('timeStamp')] = {
                            'from': e.get('from').lower(),
                            'to': e.get('to').lower()
                        }

    def get_valid_transactions(self, transactions, factors):
        valid_transactions = {}
        factor_addresses = [factor.eth_address.lower() for factor in factors]
        for transaction in transactions:
            from_address = transactions[transaction].get('from')
            to_address = transactions[transaction].get('to')
            if from_address not in factor_addresses or to_address not in factor_addresses:
                continue
            valid_transactions[transaction] = transactions[transaction]

        return valid_transactions
