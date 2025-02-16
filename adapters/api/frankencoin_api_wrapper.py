from adapters.api.frankencoin_api import FrankenCoinAPI


class FrankencoinAPIWrapper:
    _initialized: bool = False
    mint_token: dict = {}
    equity_token: dict = {}
    collateral_token_list: dict = {}

    """ Initialize """
    @classmethod
    def initialize(cls):
        if not cls._initialized:
            # Init mint token
            mint_token: dict = FrankenCoinAPI.get_prices_erc20_mint()
            cls.mint_token[mint_token["symbol"]] = mint_token

            # Init equity token
            equity_token: dict = FrankenCoinAPI.get_prices_erc20_fps()
            cls.equity_token[equity_token["symbol"]] = equity_token

            # Init collateral list
            for address, value in FrankenCoinAPI.get_prices_erc20_collateral().items():
                cls.collateral_token_list[value["symbol"]] = value

            cls._initialized = True

    """ Prices """
    @staticmethod
    def get_prices() -> dict:
        FrankencoinAPIWrapper.initialize()
        results: dict = {}
        for data in FrankenCoinAPI.get_prices_list():
            results[data["symbol"]] = {"usd": data["price"]["usd"], "chf": data["price"]["chf"]}
        return results

    @staticmethod
    def get_mint_token_price() -> dict:
        return FrankencoinAPIWrapper.get_prices()[list(FrankencoinAPIWrapper.mint_token.keys())[0]]

    @staticmethod
    def get_equity_token_price() -> dict:
        return FrankencoinAPIWrapper.get_prices()[list(FrankencoinAPIWrapper.equity_token.keys())[0]]

    @staticmethod
    def get_collateral_tokens_prices() -> dict:
        results: dict = {}
        prices: dict = FrankencoinAPIWrapper.get_prices()
        for collateral_token in FrankencoinAPIWrapper.collateral_token_list.keys():
            results[collateral_token] = prices[collateral_token]
        return results


if __name__ == "__main__":
    print(FrankencoinAPIWrapper.get_prices())