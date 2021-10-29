from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api_information.models import Shipment, Agent, Producer
from api_information.serializers import ShipmentSerializer

import requests


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

        producers = Producer.objects.all()
        agents = Agent.objects.all()

        for producer in producers:
            response = requests.get("https://api-ropsten.etherscan.io/api",
                                    params={
                                        "module": "account",
                                        "action": "txlist",
                                        "address": producer.eth_address,
                                        "tag": "latest",
                                        "apikey": "YourApiKeyToken",
                                    },
                                    headers={
                                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, '
                                                      'like Gecko) Chrome/50.0.2661.102 Safari/537.36'})
            res_status = response.json().get("status")
            if res_status == '1':
                result = response.json().get("result")
                for e in result:
                    print('from: ', e.get('from'))
                    print('to: ', e.get('to'))
                    print(e.get('input')[2:])
                    print('input', bytes.fromhex(e.get('input')[2:]).decode('utf-8'))
            print("===============")


        print(shipment_id)
        return Response(
            {"sds": "sadjsa"},
            status=status.HTTP_200_OK
        )
