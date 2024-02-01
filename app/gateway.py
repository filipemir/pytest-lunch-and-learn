from app.utils import to_query_param_str


class ThirdPartyGateway:
    async def get_a_thing(self, thing_id: str) -> dict:
        return {
            "thing_id": thing_id,
            "query_string": to_query_param_str(param_name="thing_id", param_values=[thing_id])
        }
