import os
from google.colab import drive
from google.cloud import bigquery

# ���� �Ű�����
start_diff = os.environ.get('START_DIFF', '1')
end_diff = os.environ.get('END_DIFF', '0')

# BigQuery Ŭ���̾�Ʈ ����
client = bigquery.Client()

# SQL ����
sql = f"""
SELECT refresh_date AS Day, term AS Top_Term, rank
FROM `bigquery-public-data.google_trends.top_terms`
WHERE rank = 1
  AND refresh_date BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL {start_diff} DAY)
                        AND DATE_SUB(CURRENT_DATE(), INTERVAL {end_diff} DAY)
GROUP BY Day, Top_Term, rank
ORDER BY Day, rank
"""

# ���� ����
query_job = client.query(sql)
results = query_job.result()

# ��� ���
for row in results:
    print(f"Day: {row.Day}, Top Term: {row.Top_Term}, Rank: {row.rank}")