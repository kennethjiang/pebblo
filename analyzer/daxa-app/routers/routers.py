# Copyright (c) 2024 Daxa. All rights reserved.
from api.api import App

# Create an instance of APp with a specific prefix
router_instance = App(prefix="/v1")

# Add routes to the class-based router
router_instance.router.add_api_route("/discover", App.discover, methods=["POST"], response_model=dict)
router_instance.router.add_api_route("/loader/doc", App.loader_doc, methods=["POST"], response_model=dict)
