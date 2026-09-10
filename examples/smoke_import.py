from asml_product_p3_scheduler import schedule_facility
print(schedule_facility({"n_tools": 4, "priorities": [2, 1, 1, 1]}).to_dict())
