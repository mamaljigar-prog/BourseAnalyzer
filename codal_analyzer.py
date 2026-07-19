import pandas as pd

file = "codal_output.bin"

tables = pd.read_html(file)

# صورت سود و زیان
income = tables[0]

print("===== صورت سود و زیان =====")
print(income.to_string())


# وضعیت مالی
balance = tables[4]

print("\n===== وضعیت مالی =====")
print(balance.to_string())