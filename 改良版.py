{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMzIn9YiUtpP3rMuSI7442E",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/marina554/accounting-practice/blob/main/%E6%94%B9%E8%89%AF%E7%89%88_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class Journal:\n",
        "    def __init__(self):\n",
        "        self.entries = []\n",
        "\n",
        "    def add_entry(self, entry):\n",
        "        if not isinstance(entry, JournalEntry):\n",
        "            raise ValueError(\"JournalEntryオブジェクトを渡してください\")\n",
        "        self.entries.append(entry)\n",
        "\n",
        "    def add_raw_entry(self, date, category, payment_method, amount):\n",
        "        # 生データからJournalEntryを作り追加\n",
        "        try:\n",
        "            entry = JournalEntry(date, category, payment_method, amount)\n",
        "            self.add_entry(entry)\n",
        "        except ValueError as e:\n",
        "            # エラーは警告として出力、処理は続行\n",
        "            print(f\"警告: {e}\")\n",
        "\n",
        "    def to_dataframe(self):\n",
        "        return pd.DataFrame([e.to_dict() for e in self.entries])\n",
        "\n",
        "    def total_amount(self):\n",
        "        return sum(e.amount for e in self.entries)\n",
        "\n",
        "    def total_by_category(self):\n",
        "        df = self.to_dataframe()\n",
        "        return df.groupby(\"区分\")[\"金額\"].sum()\n",
        "\n",
        "    def show_all_info(self):\n",
        "        for e in self.entries:\n",
        "            print(e.info())\n"
      ],
      "metadata": {
        "id": "C2qB_q2vmNzZ"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "journal_raw = [\n",
        "    (\"2025-11-01\", \"事務用品費\", \"現金\", 5000),\n",
        "    (\"2025-11-02\", \"旅費交通費\", \"クレジットカード\", 12000),\n",
        "    (\"2025-11-03\", \"売上\", \"銀行振込\", 30000),\n",
        "    (\"2025-11-04\", \"通信費\", \"銀行振込\", 8000),\n",
        "    (\"2025/11/05\", \"不明費用\", \"現金\", -1000),  # 不正データ\n",
        "]\n",
        "\n",
        "journal_obj = Journal()\n",
        "\n",
        "for rec in journal_raw:\n",
        "    journal_obj.add_raw_entry(*rec)\n",
        "\n",
        "# 一覧表示\n",
        "print(\"【全仕訳一覧】\")\n",
        "journal_obj.show_all_info()\n",
        "\n",
        "# DataFrame化\n",
        "df = journal_obj.to_dataframe()\n",
        "print(\"\\n【DataFrame表示】\")\n",
        "print(df)\n",
        "\n",
        "# 集計\n",
        "print(\"\\n【合計金額】\")\n",
        "print(journal_obj.total_amount())\n",
        "\n",
        "print(\"\\n【科目ごとの合計】\")\n",
        "print(journal_obj.total_by_category())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "fa155b11-80f7-4ffb-bf14-7bd07e6ee550",
        "id": "YJvak1dxnULH"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "警告: 日付が不正です: 2025/11/05\n",
            "【全仕訳一覧】\n",
            "2025-11-01: 事務用品費, 5000円 [消耗品費 / 現金]\n",
            "2025-11-02: 旅費交通費, 12000円 [旅費交通費 / 未払金]\n",
            "2025-11-03: 売上, 30000円 [普通預金 / 売上高]\n",
            "2025-11-04: 通信費, 8000円 [通信費 / 普通預金]\n",
            "\n",
            "【DataFrame表示】\n",
            "           日付   借方科目  貸方科目     金額     区分      支払方法\n",
            "0  2025-11-01   消耗品費    現金   5000  事務用品費        現金\n",
            "1  2025-11-02  旅費交通費   未払金  12000  旅費交通費  クレジットカード\n",
            "2  2025-11-03   普通預金   売上高  30000     売上      銀行振込\n",
            "3  2025-11-04    通信費  普通預金   8000    通信費      銀行振込\n",
            "\n",
            "【合計金額】\n",
            "55000\n",
            "\n",
            "【科目ごとの合計】\n",
            "区分\n",
            "事務用品費     5000\n",
            "売上       30000\n",
            "旅費交通費    12000\n",
            "通信費       8000\n",
            "Name: 金額, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "journal_obj.show_all_info()\n",
        "df = journal_obj.to_dataframe()\n",
        "print(df)\n",
        "print(journal_obj.total_amount())\n",
        "print(journal_obj.total_by_category())\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ru7LA7u7nkZV",
        "outputId": "20c26e0f-aa86-4d50-9a10-342da89e5c3e"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2025-11-01: 事務用品費, 5000円 [消耗品費 / 現金]\n",
            "2025-11-02: 旅費交通費, 12000円 [旅費交通費 / 未払金]\n",
            "2025-11-03: 売上, 30000円 [普通預金 / 売上高]\n",
            "2025-11-04: 通信費, 8000円 [通信費 / 普通預金]\n",
            "           日付   借方科目  貸方科目     金額     区分      支払方法\n",
            "0  2025-11-01   消耗品費    現金   5000  事務用品費        現金\n",
            "1  2025-11-02  旅費交通費   未払金  12000  旅費交通費  クレジットカード\n",
            "2  2025-11-03   普通預金   売上高  30000     売上      銀行振込\n",
            "3  2025-11-04    通信費  普通預金   8000    通信費      銀行振込\n",
            "55000\n",
            "区分\n",
            "事務用品費     5000\n",
            "売上       30000\n",
            "旅費交通費    12000\n",
            "通信費       8000\n",
            "Name: 金額, dtype: int64\n"
          ]
        }
      ]
    }
  ]
}
