
import pandas as pd

def main():
    # Читаем Excel-файл
    df = pd.read_csv('data.csv')

    # Добавляем колонку с суммой продажи
    df['Сумма'] = df['Количество'] * df['Цена']

    # Группируем по категориям и считаем общую выручку
    report = df.groupby('Категория', as_index=False)['Сумма'].sum()
    report = report.sort_values('Сумма', ascending=False)

    # Сохраняем результат в новый Excel-файл
    report.to_excel('sales_summary.xlsx', index=False)

    # Выводим результат в консоль
    print("Отчёт сохранён в sales_summary.xlsx")
    print(report)

if __name__ == '__main__':
    main()
    
