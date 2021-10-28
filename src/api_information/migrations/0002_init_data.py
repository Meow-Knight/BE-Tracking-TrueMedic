# Generated by Django 3.2.8 on 2021-10-28 19:51

from django.db import migrations


def initial_producer_data(apps, schema_editor):
    producer_model = apps.get_model("api_information", "Producer")
    producers = [producer_model(business_code='LLP7-P4NF-D9AV-U98I',
                                eth_address='0x8ff4c1b83857A327C73F499Dfd54B23864E812D9',
                                name='Công ty Dược phẩm và Thương mại Phương Đông',
                                address="Cụm Công nghiệp Hạp Lĩnh, phường Hạp Lĩnh, thành phố Bắc Ninh",
                                email="duocpham@phuongdong.com",
                                phone="0123456789"),
                 producer_model(business_code='QKWX-1E9F-KZFO-WTDD',
                                eth_address='0xc03efF7f010fe79F3fB9f0242Bf8fFEc4a043D6c',
                                name='Công ty cổ phần Traphaco',
                                address="Ngõ 15, Đường Ngọc Hồi, P.Hoàng Liệt, Q.Hoàng Mai, Hà Nội",
                                email="info@traphaco.com.vn",
                                phone="18006612"),
                 producer_model(business_code='3DKL-9ZSN-3LS9-LFG5',
                                eth_address='0xc03efF7f010fe79F3fB9f0242Bf8fFE999999999',
                                name='Công ty cổ phần PYMEPHARCO',
                                address="166 – 170 Nguyễn Huệ, Tuy Hòa, Phú Yên",
                                email="info@pymephaco.com.vn",
                                phone="02573823228")]

    producer_model.objects.bulk_create(producers)


def initial_agent_data(apps, schema_editor):
    agent_model = apps.get_model("api_information", "Agent")
    agents = [agent_model(business_code='3DKL-9ZSN-3LS9-LFG5',
                          eth_address='0xe6Aa957Da0f42D51bD15b96999A71F17E18211Bf',
                          name='Nhà thuốc Hồng Mai',
                          address="Số 85, phố Hồng Mai, phường Quỳnh Lôi, quận Hai Bà Trưng, thành phố Hà Nội"),
              agent_model(business_code='K1P9-XY0G-7IOC-DKD6',
                          eth_address='0xc03efF7f010fe79F3fB9f0242Bf8fFE666666666',
                          name='Nhà thuốc Minh Phúc',
                          address="Số 3 ngõ 23 đường Xuân La, phường Xuân La, quận Tây Hồ, thành phố Hà Nội"),
              ]

    agent_model.objects.bulk_create(agents)


def initial_medicine_data(apps, schema_editor):
    medicine_model = apps.get_model("api_information", "Medicine")
    medicine_1 = medicine_model(name='Tinh Dầu Hoa Anh Thảo Blackmores',
                                image="https://res.cloudinary.com/ddqzgiilu/image/upload/v1635451766/TrueMedic/tinh-dau-hoa-anh-thao-blackmores_risjqa.jpg",
                                unit="Chai")
    medicine_2 = medicine_model(name='Viên Bio Island Lysine Của Úc',
                                image="https://res.cloudinary.com/ddqzgiilu/image/upload/v1635452030/TrueMedic/vien-uong-bio-island-lysine_wblubn.png",
                                unit="Chai")
    medicine_3 = medicine_model(name='Nước Đông Trùng Hạ Thảo KangHwa',
                                image="https://res.cloudinary.com/ddqzgiilu/image/upload/v1635452175/TrueMedic/nuoc-dong-trung-ha-thao-kanghwa_vtpvl9.jpg",
                                unit="Hộp")
    medicine_4 = medicine_model(name='Trà Đông Trùng Hạ Thảo Vinh Gia',
                                image="https://res.cloudinary.com/ddqzgiilu/image/upload/v1635452240/TrueMedic/tra-dong-trung-ha-thao-vinh-gia_mapfmb.jpg",
                                unit="Hộp")
    medicine_1.save()
    medicine_2.save()
    medicine_3.save()
    medicine_4.save()

    shipment_model = apps.get_model("api_information", "Shipment")
    shipments = [shipment_model(medicine=medicine_1,
                                quantity=100),
                 shipment_model(medicine=medicine_1,
                                quantity=200),
                 shipment_model(medicine=medicine_1,
                                quantity=300),
                 shipment_model(medicine=medicine_2,
                                quantity=150),
                 shipment_model(medicine=medicine_2,
                                quantity=200),
                 shipment_model(medicine=medicine_2,
                                quantity=200),
                 shipment_model(medicine=medicine_3,
                                quantity=50),
                 shipment_model(medicine=medicine_4,
                                quantity=500),
                 ]

    shipment_model.objects.bulk_create(shipments)


class Migration(migrations.Migration):
    dependencies = [
        ('api_information', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial_producer_data, migrations.RunPython.noop),
        migrations.RunPython(initial_agent_data, migrations.RunPython.noop),
        migrations.RunPython(initial_medicine_data, migrations.RunPython.noop),
    ]
