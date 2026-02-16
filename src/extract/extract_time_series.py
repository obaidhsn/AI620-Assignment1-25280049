from pytrends.request import TrendReq
import time
from pathlib import Path


class TimeSeriesExtractor:
    def __init__(self):
        pass

    def google_trends_extractor(self, keywords: list, output_file_path: str, 
                                geo: str = None, timeframe: str = 'today 1-y'):
        output_path = Path(output_file_path)

        self.pytrends = TrendReq(
            hl="en-US",
            tz=360,
            retries=3,
            backoff_factor=0.2
        )
        self.geo = geo
        self.timeframe = timeframe

        self.pytrends.build_payload(
            kw_list=keywords,
            geo=self.geo,
            timeframe=self.timeframe
        )

        time.sleep(5)

        df = self.pytrends.interest_over_time()

        if "isPartial" in df.columns:
            df = df.drop(columns=["isPartial"])

        df.to_csv(output_path)

        print("Google Trends data extracted successfully.")
        return df
