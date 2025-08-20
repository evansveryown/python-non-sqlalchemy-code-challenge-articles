class Article:
    all = []  # class variable to track all articles

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("Author must be an Author")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be a Magazine")

        self.author = author
        self.magazine = magazine

        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be string 5–50 chars")
        self._title = title

        # Add each new article to the class-level list
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # Ignore attempts to reset title
        pass


class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name.strip()) == 0:
            raise Exception("Name cannot be empty")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Ignore any attempts to change name (immutability)
        pass

    # 🔹 Required methods
    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list({article.magazine.category for article in self.articles()})


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Name must be a string 2–16 chars")
        if not isinstance(category, str) or not (len(category) > 0):
            raise Exception("Category must be a non-empty string")

        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # ✅ silently ignore bad values instead of raising
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        # ✅ silently ignore bad values instead of raising
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        return [article.title for article in self.articles()] or None

    def contributing_authors(self):
        # authors who have written more than 2 articles for this magazine
        authors = [article.author for article in self.articles()]
        return list({author for author in authors if authors.count(author) > 2}) or None
