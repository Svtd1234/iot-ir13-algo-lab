#!/bin/bash
# Script to create lab1-lab9 branches with unique Readme.md files
# Run this script from the root of the repository

set -e

declare -A TOPICS=(
  [1]="Вступ до алгоритмів та складності обчислень"
  [2]="Алгоритми сортування (бульбашкове, вставками, злиттям)"
  [3]="Алгоритми пошуку (лінійний, бінарний)"
  [4]="Структури даних: стек та черга"
  [5]="Зв'язані списки та операції над ними"
  [6]="Дерева та алгоритми їх обходу"
  [7]="Графи та алгоритми пошуку (BFS, DFS)"
  [8]="Динамічне програмування"
  [9]="Жадібні алгоритми та їх застосування"
)

BASE_BRANCH=$(git symbolic-ref --short HEAD)
echo "Creating lab branches from: $BASE_BRANCH"

for i in $(seq 1 9); do
  BRANCH="lab$i"
  TOPIC="${TOPICS[$i]}"

  echo "Creating branch: $BRANCH"

  git checkout -b "$BRANCH" 2>/dev/null || git checkout "$BRANCH"

  python3 - << PYEOF
num = $i
topic = """${TOPIC}"""
lines = [
    f"# Лабораторна робота #{num}",
    "",
    f"## Тема: {topic}",
    "",
    "## Опис",
    f"Це гілка для виконання лабораторної роботи #{num} з курсу",
    '"Алгоритми та структури даних" (iot-ir13-algo-lab).',
    "",
    "## Мета роботи",
    "Ознайомлення з основними алгоритмами та структурами даних",
    "у контексті Інтернету речей (IoT).",
    "",
    f"## Завдання лабораторної роботи #{num}",
    f"1. Вивчити теоретичний матеріал з теми: **{topic}**",
    "2. Реалізувати алгоритм відповідно до варіанту завдання",
    "3. Провести аналіз часової та просторової складності алгоритму",
    "4. Перевірити коректність роботи програми на тестових прикладах",
    "5. Підготувати звіт про виконану роботу",
    "",
    "## Структура гілки",
    "\`\`\`",
    f"lab{num}/",
    "├── Readme.md       # Опис лабораторної роботи",
    "└── src/            # Вихідний код",
    "\`\`\`",
    "",
    "## Технічні вимоги",
    "- Мова програмування: Python / C / C++",
    "- Документація коду обов'язкова",
    "- Результати тестування мають бути збережені",
    "",
    "## Оцінювання",
    "| Критерій | Бали |",
    "|----------|------|",
    "| Виконання завдання | 60 |",
    "| Якість коду | 20 |",
    "| Звіт та документація | 20 |",
    "",
    "## Автор",
    "Студент групи iot-ir13",
    "",
    "## Курс",
    "Алгоритми та структури даних — iot-ir13-algo-lab",
]
with open("Readme.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")
print(f"Readme.md written for lab{num}")
PYEOF

  git add Readme.md
  git commit -m "Add Readme.md for lab$i: $TOPIC"
  git push origin "$BRANCH"

  git checkout "$BASE_BRANCH"
  echo "Branch $BRANCH created and pushed successfully"
done

echo ""
echo "All 9 lab branches (lab1-lab9) created and pushed to GitHub!"
