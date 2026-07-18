from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # 应用配置
    app_name: str = "Customer Service Agent"

    app_version: str = "0.1.0"

    app_port: int = 8000

    debug: bool = True


    # DeepSeek配置

    deepseek_api_key: str = ""

    deepseek_base_url: str = "https://api.deepseek.com"

    deepseek_model: str = "deepseek-chat"



    # MySQL配置

    mysql_host: str = "localhost"

    mysql_port: int = 3306

    mysql_user: str = "root"

    mysql_password: str = ""

    mysql_database: str = "customer_service"



    model_config = SettingsConfigDict(

        env_file=".env",

        env_file_encoding="utf-8",

        extra="ignore"

    )



settings = Settings()