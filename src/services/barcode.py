import httpx


async def get_product_name_from_barcode(barcode_number: int) -> str:
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.get(
            f"https://m.retaildb.or.kr/service/product_info/search/{barcode_number}"
        )

        data = response.json()

    return data["baseItems"][-1]["value"]
