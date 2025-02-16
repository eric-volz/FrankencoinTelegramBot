import requests


class FrankenCoinAPI:
    BASE_URL: str = "https://api.frankencoin.com"

    @staticmethod
    def _get(endpoint: str) -> dict:
        """Generic GET request method."""
        response = requests.get(f"{FrankenCoinAPI.BASE_URL}{endpoint}")
        response.raise_for_status()
        return response.json()

    # Positions endpoints
    @staticmethod
    def get_positions_list() -> dict:
        return FrankenCoinAPI._get("/positions/list")

    @staticmethod
    def get_positions_mapping() -> dict:
        return FrankenCoinAPI._get("/positions/mapping")

    @staticmethod
    def get_positions_open() -> dict:
        return FrankenCoinAPI._get("/positions/open")

    @staticmethod
    def get_positions_requests() -> dict:
        return FrankenCoinAPI._get("/positions/requests")

    @staticmethod
    def get_positions_owners() -> dict:
        return FrankenCoinAPI._get("/positions/owners")

    @staticmethod
    def get_positions_mintingupdates_list() -> dict:
        return FrankenCoinAPI._get("/positions/mintingupdates/list")

    @staticmethod
    def get_positions_mintingupdates_mapping() -> dict:
        return FrankenCoinAPI._get("/positions/mintingupdates/mapping")

    # Ecosystem endpoints
    @staticmethod
    def get_ecosystem_frankencoin_minter_list() -> dict:
        return FrankenCoinAPI._get("/ecosystem/frankencoin/minter/list")

    @staticmethod
    def get_ecosystem_frankencoin_minter_mapping() -> dict:
        return FrankenCoinAPI._get("/ecosystem/frankencoin/minter/mapping")

    @staticmethod
    def get_ecosystem_collateral_list() -> dict:
        return FrankenCoinAPI._get("/ecosystem/collateral/list")

    @staticmethod
    def get_ecosystem_collateral_mapping() -> dict:
        return FrankenCoinAPI._get("/ecosystem/collateral/mapping")

    @staticmethod
    def get_ecosystem_collateral_positions() -> dict:
        return FrankenCoinAPI._get("/ecosystem/collateral/positions")

    @staticmethod
    def get_ecosystem_collateral_positions_details() -> dict:
        return FrankenCoinAPI._get("/ecosystem/collateral/positions/details")

    @staticmethod
    def get_ecosystem_collateral_stats() -> dict:
        return FrankenCoinAPI._get("/ecosystem/collateral/stats")

    @staticmethod
    def get_ecosystem_fps_info() -> dict:
        return FrankenCoinAPI._get("/ecosystem/fps/info")

    @staticmethod
    def get_ecosystem_frankencoin_info() -> dict:
        return FrankenCoinAPI._get("/ecosystem/frankencoin/info")

    @staticmethod
    def get_ecosystem_frankencoin_keyvalues() -> dict:
        return FrankenCoinAPI._get("/ecosystem/frankencoin/keyvalues")

    @staticmethod
    def get_ecosystem_frankencoin_mintburnmapping() -> dict:
        return FrankenCoinAPI._get("/ecosystem/frankencoin/mintburnmapping")

    # Savings endpoints
    @staticmethod
    def get_savings_leadrate_info() -> dict:
        return FrankenCoinAPI._get("/savings/leadrate/info")

    @staticmethod
    def get_savings_leadrate_rates() -> dict:
        return FrankenCoinAPI._get("/savings/leadrate/rates")

    @staticmethod
    def get_savings_leadrate_proposals() -> dict:
        return FrankenCoinAPI._get("/savings/leadrate/proposals")

    @staticmethod
    def get_savings_core_info() -> dict:
        return FrankenCoinAPI._get("/savings/core/info")

    @staticmethod
    def get_savings_core_balances() -> dict:
        return FrankenCoinAPI._get("/savings/core/balances")

    @staticmethod
    def get_savings_core_user(address: str) -> dict:
        return FrankenCoinAPI._get(f"/savings/core/user/{address}")

    # Prices endpoints
    @staticmethod
    def get_prices_list() -> dict:
        return FrankenCoinAPI._get("/prices/list")

    @staticmethod
    def get_prices_mapping() -> dict:
        return FrankenCoinAPI._get("/prices/mapping")

    @staticmethod
    def get_prices_erc20_mint() -> dict:
        return FrankenCoinAPI._get("/prices/erc20/mint")

    @staticmethod
    def get_prices_erc20_fps() -> dict:
        return FrankenCoinAPI._get("/prices/erc20/fps")

    @staticmethod
    def get_prices_erc20_collateral() -> dict:
        return FrankenCoinAPI._get("/prices/erc20/collateral")

    # Challenges endpoints
    @staticmethod
    def get_challenges_list() -> dict:
        return FrankenCoinAPI._get("/challenges/list")

    @staticmethod
    def get_challenges_mapping() -> dict:
        return FrankenCoinAPI._get("/challenges/mapping")

    @staticmethod
    def get_challenges_challengers() -> dict:
        return FrankenCoinAPI._get("/challenges/challengers")

    @staticmethod
    def get_challenges_positions() -> dict:
        return FrankenCoinAPI._get("/challenges/positions")

    @staticmethod
    def get_challenges_prices() -> dict:
        return FrankenCoinAPI._get("/challenges/prices")

    @staticmethod
    def get_challenges_bids_list() -> dict:
        return FrankenCoinAPI._get("/challenges/bids/list")

    @staticmethod
    def get_challenges_bids_mapping() -> dict:
        return FrankenCoinAPI._get("/challenges/bids/mapping")

    @staticmethod
    def get_challenges_bids_bidders() -> dict:
        return FrankenCoinAPI._get("/challenges/bids/bidders")

    @staticmethod
    def get_challenges_bids_challenges() -> dict:
        return FrankenCoinAPI._get("/challenges/bids/challenges")

    @staticmethod
    def get_challenges_bids_positions() -> dict:
        return FrankenCoinAPI._get("/challenges/bids/positions")

    # Analytics endpoints
    @staticmethod
    def get_analytics_profit_loss_log() -> dict:
        return FrankenCoinAPI._get("/analytics/profitLossLog")

    @staticmethod
    def get_analytics_transaction_log_json() -> dict:
        return FrankenCoinAPI._get("/analytics/transactionLog/json")

    @staticmethod
    def get_analytics_transaction_log_csv_e18() -> dict:
        return FrankenCoinAPI._get("/analytics/transactionLog/csvE18")

    @staticmethod
    def get_analytics_daily_log_json() -> dict:
        return FrankenCoinAPI._get("/analytics/dailyLog/json")

    @staticmethod
    def get_analytics_daily_log_csv_e18() -> dict:
        return FrankenCoinAPI._get("/analytics/dailyLog/csvE18")

    @staticmethod
    def get_analytics_fps_exposure() -> dict:
        return FrankenCoinAPI._get("/analytics/fps/exposure")

    @staticmethod
    def get_analytics_fps_earnings() -> dict:
        return FrankenCoinAPI._get("/analytics/fps/earnings")