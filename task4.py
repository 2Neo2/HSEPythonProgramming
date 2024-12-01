import csv

# Task 1.
def read_purchase_log(filepath):
    purchases = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            next(f)

            for line in f:
                line = line.strip()
                if line:
                    user_id, category = line.split(',')
                    purchases[user_id] = category
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}
    return purchases


purchases = read_purchase_log('storage/logs/purchase_log.txt')


if purchases:
    for user_id, category in purchases.items():
        print(f"{user_id} ‘{category}’")


#==============================
# Task 2.


def add_purchase_category(visit_log_path, purchase_log_path, funnel_path):
    purchases = {}
    try:
      with open(purchase_log_path, 'r', encoding='utf-8') as f:
          next(f)

          for line in f:
              user_id, category = line.strip().split(',')
              purchases[user_id] = category
    except FileNotFoundError:
        print(f"Error: File {purchase_log_path} not found.")
        return
    except Exception as e:
        print(f"Error: {e}")
        return


    with open(visit_log_path, 'r', encoding='utf-8') as visit_log, \
            open(funnel_path, 'w', encoding='utf-8', newline='') as funnel:

        reader = csv.reader(visit_log, delimiter=',')
        writer = csv.writer(funnel, delimiter=',')
        writer.writerow(['user_id', 'source', 'category'])

        next(reader)
        for row in reader:
            user_id = row[0]
            if user_id in purchases:
                row.append(purchases[user_id])
                writer.writerow(row)


visit_log_path = 'storage/logs/visit_log.csv'
purchase_log_path = 'storage/logs/purchase_log.txt'
funnel_path = 'storage/logs/funnel.csv'

add_purchase_category(visit_log_path, purchase_log_path, funnel_path)
