from asyncio import sleep


async def async_addition(a: int, b: int):
    await sleep(1)
    return a + b

def to_query_param_str(param_name: str, param_values: list[str]) -> str:
    chunks = [f"{param_name}={param_value}" for param_value in param_values]
    return f"?{'&'.join(chunks)}"

