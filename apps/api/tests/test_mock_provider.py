from uuid import uuid4

from app.integrations.pricing.mock import MockPricingProvider


def test_mock_provider_returns_price():
    provider = MockPricingProvider(seed=1)
    result = provider.fetch_price(uuid4())

    assert result.value > 0
    assert result.currency == "USD"
    assert 0 <= (result.confidence or 0) <= 1
