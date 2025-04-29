import random

class MemoryGame:
    def __init__(self, n, m, categories):
        """
        מאתחל את משחק הזיכרון.

        ארגומנטים:
            n (int): מספר השורות ברשת.
            m (int): מספר העמודות ברשת.
            categories (list): רשימה של רשימות, כאשר כל רשימה פנימית
                                מכילה פריטים עבור קטגוריה (למשל, צבעים).
        """
        if (n * m) % 2 != 0:
            raise ValueError("מספר התאים הכולל (n * m) חייב להיות זוגי.")
        if n % 2 != 0 and m % 2 != 0:
            raise ValueError("או n או m (או שניהם) חייבים להיות זוגיים.")

        self.n = n
        self.m = m
        self.grid = []
        self.revealed = [[False for _ in range(m)] for _ in range(n)]
        self.matched = [[False for _ in range(m)] for _ in range(n)]
        self.num_guesses = 0
        self.available_categories = categories
        self.selected_category = random.choice(self.available_categories)
        self._initialize_grid(self.selected_category)

    def _initialize_grid(self, category):
        """
        מאתחל את הרשת עם ערכים מזווגים מהקטגוריה הנבחרת ומערבב אותה.
        """
        num_pairs = (self.n * self.m) // 2
        if len(category) < num_pairs:
            raise ValueError(f"אין מספיק פריטים בקטגוריה הנבחרת. דרושים לפחות {num_pairs} פריטים ייחודיים.")

        items = random.sample(category, num_pairs)
        grid_values = items * 2
        random.shuffle(grid_values)

        index = 0
        for r in range(self.n):
            row = []
            for c in range(self.m):
                row.append(grid_values[index])
                index += 1
            self.grid.append(row)

    def display_grid(self):
        """
        מציג את המצב הנוכחי של הרשת.
        תאים גלויים מציגים את ערכיהם, אחרים מציגים '?'.
        """
        print("-" * (self.m * 4 + 1))
        for r in range(self.n):
            row_str = "| "
            for c in range(self.m):
                if self.revealed[r][c] or self.matched[r][c]:
                    row_str += f"{self.grid[r][c]:<2} | "
                else:
                    row_str += "?  | "
            print(row_str)
            print("-" * (self.m * 4 + 1))

    def select_cells(self, r1, c1, r2, c2):
        """
        מטפל בבחירת שני תאים על ידי השחקן.

        ארגומנטים:
            r1, c1 (int): קואורדינטות התא הראשון.
            r2, c2 (int): קואורדינטות התא השני.

        החזרות:
            bool: True אם התאים הנבחרים תואמים, False אחרת.
        """
        if not self._is_valid_selection(r1, c1) or not self._is_valid_selection(r2, c2):
            print("בחירה לא חוקית. אנא הזן מספרי שורה ועמודה חוקיים עבור תאים שטרם נחשפו.")
            return False

        if r1 == r2 and c1 == c2:
            print("בחרת באותו תא פעמיים. אנא בחר בשני תאים שונים.")
            return False

        # חשיפת התאים הנבחרים באופן זמני
        self.revealed[r1][c1] = True
        self.revealed[r2][c2] = True
        self.num_guesses += 1

        self.display_grid()

        if self.grid[r1][c1] == self.grid[r2][c2]:
            print("נמצאה התאמה!")
            self.matched[r1][c1] = True
            self.matched[r2][c2] = True
            return True
        else:
            print("אין התאמה. נסה שוב.")
            # סטטוס החשיפה יאופס בתור הבא אם לא נמצאה התאמה
            return False

    def _is_valid_selection(self, r, c):
        """
        בדיקה האם הקואורדינטות הנתונות חוקיות והתא טרם הותאם.
        """
        return 0 <= r < self.n and 0 <= c < self.m and not self.matched[r][c]

    def reset_revealed(self):
        """
        מאפס את סטטוס החשיפה של תאים שאינם תואמים.
        נקרא לאחר כל תור אם לא נמצאה התאמה.
        """
        for r in range(self.n):
            for c in range(self.m):
                if not self.matched[r][c]:
                    self.revealed[r][c] = False

    def is_game_over(self):
        """
        בדיקה האם המשחק הסתיים (כל התאים הותאמו).

        החזרות:
            bool: True אם המשחק הסתיים, False אחרת.
        """
        for r in range(self.n):
            for c in range(self.m):
                if not self.matched[r][c]:
                    return False
        return True

    def get_performance_stats(self):
        """
        מחזיר את מספר הניחושים שביצע השחקן.

        החזרות:
            int: מספר הניחושים.
        """
        return self.num_guesses

    def play(self):
        """
        לולאת המשחק הראשית.
        """
        print("ברוכים הבאים למשחק הזיכרון!")
        print(f"קטגוריה: {', '.join(self.selected_category)}")
        print("נסה למצוא את הזוגות התואמים.")

        while not self.is_game_over():
            self.display_grid()
            print(f"ניחושים: {self.num_guesses}")

            try:
                r1 = int(input(f"הזן את השורה עבור התא הראשון (0 עד {self.n - 1}): "))
                c1 = int(input(f"הזן את העמודה עבור התא הראשון (0 עד {self.m - 1}): "))
                r2 = int(input(f"הזן את השורה עבור התא השני (0 עד {self.n - 1}): "))
                c2 = int(input(f"הזן את העמודה עבור התא השני (0 עד {self.m - 1}): "))
            except ValueError:
                print("קלט לא חוקי. אנא הזן מספרים.")
                self.reset_revealed()
                continue

            if self.select_cells(r1, c1, r2, c2):
                pass  # אם נמצאה התאמה, התאים נשארים גלויים
            else:
                self.reset_revealed()

        print("\nמזל טוב! התאמת את כל הזוגות.")
        self.display_grid()
        print(f"סיימת את המשחק ב-{self.get_performance_stats()} ניחושים.")

# שיקולי אמינות, תחזוקתיות, וסילוּמיוּת:

# אמינות:
# 1. ולידציית קלט: שיטת `select_cells` כוללת בדיקות כדי לוודא שקואורדינטות הקלט של
#    השחקן נמצאות בתוך גבולות הרשת וששני התאים הנבחרים אינם זהים וטרם הותאמו.
#    זה מונע מהתוכנית לקרוס עקב קלט לא חוקי.
# 2. טיפול בשגיאות: שיטת `play` משתמשת במבנה `try-except` כדי לטפל בשגיאת
#    `ValueError` אם המשתמש מזין קלט שאינו מספרי לבחירת תא.
# 3. ניהול מצב המשחק: מערכי הדו-ממד `revealed` ו-`matched` עוקבים במדויק אחר מצב
#    כל תא, מה שמבטיח שלוגיקת המשחק פועלת על המידע הנכון.

# תחזוקתיות:
# 1. עיצוב מודולרי: הקוד מאורגן בתוך מחלקה (`MemoryGame`) עם שיטות מוגדרות היטב,
#    אשר כל אחת אחראית על חלק ספציפי בלוגיקת המשחק (למשל, `_initialize_grid`,
#    `display_grid`, `select_cells`). זה הופך את הקוד לקל יותר להבנה, ניפוי באגים,
#    ושינוי.
# 2. שמות שיטות והערות ברורים: שמות השיטות תיאוריים, ומצביעים על מטרתן. הערות
#    משמשות להסברת הפונקציונליות של שיטות וקטעי קוד חשובים.
# 3. הפרדת דאגות: לוגיקת המשחק מופרדת מממשק המשתמש (אף על פי שממשק המשתמש כאן
#    הוא פשוט מבוסס טקסט). זה הופך את שינוי ממשק המשתמש בעתיד לקל יותר באופן
#    פוטנציאלי, מבלי להשפיע על מכניקת הליבה של המשחק.
# 4. שימוש בפרמטרים: שיטת `__init__` מקבלת את `n`, `m`, ו-`categories` כפרמטרים,
#    מה שהופך את מחלקת `MemoryGame` לניתנת לשימוש חוזר עבור גדלי רשת ותוכן שונים.

# סילוּמיוּת (Scalability):
# 1. תוכן מבוסס קטגוריות: ניתן להגדיל בקלות את המשחק כדי לכלול קטגוריות נוספות
#    על ידי הוספתן לרשימה `available_categories`. שיטת `_initialize_grid`
#    מתוכננת לעבוד עם כל קטגוריה, בתנאי שיש בה מספיק פריטים ייחודיים לגודל הרשת.
# 2. גודל רשת ניתן להתאמה: הקוד מטפל בערכים חוקיים שרירותיים עבור `n` ו-`m`.
#    מבני הנתונים (כמו `grid`, `revealed`, `matched`) נוצרים באופן דינמי
#    בהתבסס על `n` ו-`m`, מה שמאפשר לשחק את המשחק על גבי רשתות בגדלים שונים.
# 3. פוטנציאל לתכונות נוספות: המבנה הנוכחי מספק בסיס טוב להוספת תכונות נוספות
#    בעתיד, כגון:
#     - מצבי משחק שונים (למשל, מוגבל בזמן).
#     - מספר שחקנים.
#     - ממשק משתמש גרפי (GUI).
#     - שמירה וטעינה של התקדמות המשחק.
# 4. יעילות עבור רשתות גדולות יותר (שיקול): עבור רשתות גדולות מאוד, התצוגה הנוכחית
#    מבוססת הטקסט עשויה להיות פחות פרקטית. ממשק משתמש גרפי יהווה פתרון סילוּמִי
#    יותר עבור ויזואליזציה במקרים כאלה. לוגיקת הליבה של המשחק הקשורה להתאמה
#    וניהול מצב המשחק אמורה להישאר יעילה מספיק עבור רשתות גדולות באופן סביר.

if __name__ == "__main__":
    # דוגמה לשימוש:
    categories = [
        ["אדום", "כחול", "ירוק", "צהוב", "סגול", "כתום", "ורוד", "חום"],
        ["תפוח", "בננה", "דובדבן", "תמר", "סמבוק", "תאנה", "ענבים", "מלון"],
        ["מכונית", "אופניים", "אוטובוס", "רכבת", "מטוס", "סירה", "רכבת_תחתית", "משאית"]
    ]

    while True:
        try:
            n = int(input("הזן את מספר השורות (N, לפחות אחד מ-N או M חייב להיות זוגי): "))
            m = int(input("הזן את מספר העמודות (M, לפחות אחד מ-N או M חייב להיות זוגי): "))
            game = MemoryGame(n, m, categories)
            break
        except ValueError as e:
            print(e)
            print("אנא נסה שוב עם מימדים חוקיים.")

    game.play()