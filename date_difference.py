from datetime import datetime

start_date = datetime(2024, 1, 1)
end_date = datetime.now()

difference = end_date - start_date
print(f"Gün farkı: {difference.days}")
