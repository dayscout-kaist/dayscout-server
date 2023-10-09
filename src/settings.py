from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ES_URL: str = "http://bap.sparcs.org:31007"
    ES_INDEX: str = "nutrient_ver_02"

    CLOVA_API_URL: str = "https://5xcfpcnwfi.apigw.ntruss.com/custom/v1/25058/038a80468ee57106c9c2c789de5ad7a69b576c0bef74fa695e4dc7db1767d967/general"
    CLOVA_CLIENT_SECRET: str


settings = Settings(_env_file=".env")
