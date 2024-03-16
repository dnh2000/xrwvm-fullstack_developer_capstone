from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description'])) # pylint: disable=line-too-long

    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
      {"name": "Pathfinder", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]}, # pylint: disable=line-too-long
      {"name": "Qashqai", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]}, # pylint: disable=line-too-long
      {"name": "XTRAIL", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]}, # pylint: disable=line-too-long
      {"name": "A-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1]}, # pylint: disable=line-too-long
      {"name": "C-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1]}, # pylint: disable=line-too-long
      {"name": "E-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1]}, # pylint: disable=line-too-long
      {"name": "A4", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]}, # pylint: disable=line-too-long
      {"name": "A5", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]}, # pylint: disable=line-too-long
      {"name": "A6", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]}, # pylint: disable=line-too-long
      {"name": "Sorrento", "type": "SUV", "year": 2023, "car_make": car_make_instances[3]}, # pylint: disable=line-too-long
      {"name": "Carnival", "type": "SUV", "year": 2023, "car_make": car_make_instances[3]}, # pylint: disable=line-too-long
      {"name": "Cerato", "type": "Sedan", "year": 2023, "car_make": car_make_instances[3]}, # pylint: disable=line-too-long
      {"name": "Corolla", "type": "Sedan", "year": 2023, "car_make": car_make_instances[4]}, # pylint: disable=line-too-long
      {"name": "Camry", "type": "Sedan", "year": 2023, "car_make": car_make_instances[4]}, # pylint: disable=line-too-long
      {"name": "Kluger", "type": "SUV", "year": 2023, "car_make": car_make_instances[4]}, # pylint: disable=line-too-long
    ]

    for data in car_model_data:
        CarModel.objects.create(name=data['name'], car_make=data['car_make'], type=data['type'], year=data['year'])
