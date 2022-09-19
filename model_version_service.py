from functools import lru_cache


class ModelVersionService:
    @lru_cache(maxsize=20)
    def get_model_version(self, source_lang: str, target_lang: str) -> str:
        print(f"get_model_version called with source_lang {source_lang}, target_lang {target_lang}")
        return "1.2.3"
