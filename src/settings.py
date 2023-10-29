from pydantic import BaseSettings, ValidationError


class Settings(BaseSettings):
    ES_URL: str = "http://bap.sparcs.org:31007"
    ES_INDEX: str = "nutrient_ver_02"
    CLOVA_API_URL: str = "https://5xcfpcnwfi.apigw.ntruss.com/custom/v1/25058/038a80468ee57106c9c2c789de5ad7a69b576c0bef74fa695e4dc7db1767d967/general"
    CLOVA_CLIENT_SECRET: str
    USER_NAME: str = "root"
    DB_PASSWORD: str
    HOST_NAME: str = "127.0.0.1"
    DB_NAME: str = "user_db"

    class Config:
        env_file = ".env"


try:
    settings = Settings()
    print(settings.ES_URL)  # 예를 들면 환경 변수에서 로드된 값
except ValidationError as e:
    print("환경 변수 설정 오류:", e)
