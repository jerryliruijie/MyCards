from app.integrations.pricing.base import PricingProvider
from app.integrations.pricing.mock import MockPricingProvider


def get_pricing_provider(provider_key: str) -> PricingProvider:
    # TODO: route provider keys to real external adapters as they are added.
    if provider_key == MockPricingProvider.provider_key:
        return MockPricingProvider()
    raise ValueError(f"Unknown pricing provider: {provider_key}")
