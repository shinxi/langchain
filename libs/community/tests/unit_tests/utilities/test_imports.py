from langchain_community.utilities import __all__, _module_lookup

EXPECTED_ALL = [
    "AlphaVantageAPIWrapper",
    "ApifyWrapper",
    "ArceeWrapper",
    "ArxivAPIWrapper",
    "AskNewsAPIWrapper",
    "BibtexparserWrapper",
    "BingSearchAPIWrapper",
    "BraveSearchWrapper",
    "DataheraldAPIWrapper",
    "DuckDuckGoSearchAPIWrapper",
    "DriaAPIWrapper",
    "GoldenQueryAPIWrapper",
    "GoogleFinanceAPIWrapper",
    "GoogleJobsAPIWrapper",
    "GoogleLensAPIWrapper",
    "GooglePlacesAPIWrapper",
    "GoogleScholarAPIWrapper",
    "GoogleSearchAPIWrapper",
    "GoogleSerperAPIWrapper",
    "GoogleTrendsAPIWrapper",
    "GraphQLAPIWrapper",
    "InfobipAPIWrapper",
    "JiraAPIWrapper",
    "LambdaWrapper",
    "MaxComputeAPIWrapper",
    "MetaphorSearchAPIWrapper",
    "NasaAPIWrapper",
    "RivaASR",
    "RivaTTS",
    "AudioStream",
    "NVIDIARivaASR",
    "NVIDIARivaTTS",
    "NVIDIARivaStream",
    "OpenWeatherMapAPIWrapper",
    "OracleSummary",
    "OutlineAPIWrapper",
    "NutritionAIAPI",
    "Portkey",
    "PowerBIDataset",
    "PubMedAPIWrapper",
    "Requests",
    "RequestsWrapper",
    "RememberizerAPIWrapper",
    "SQLDatabase",
    "SceneXplainAPIWrapper",
    "SearchApiAPIWrapper",
    "SearxSearchWrapper",
    "SerpAPIWrapper",
    "SparkSQL",
    "StackExchangeAPIWrapper",
    "SteamWebAPIWrapper",
    "TensorflowDatasets",
    "TextRequestsWrapper",
    "TwilioAPIWrapper",
    "WikipediaAPIWrapper",
    "WolframAlphaAPIWrapper",
    "YouSearchAPIWrapper",
    "ZapierNLAWrapper",
    "MerriamWebsterAPIWrapper",
    "MojeekSearchAPIWrapper",
]


def test_all_imports() -> None:
    assert set(__all__) == set(EXPECTED_ALL)
    assert set(__all__) == set(_module_lookup.keys())