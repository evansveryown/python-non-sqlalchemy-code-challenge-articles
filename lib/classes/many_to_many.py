from collections import Counter


class Article:
    all = []  # class variable to track all articles

    def __init__(self, author, magazine, title):
        self.author = author      # goes through property setter
        self.magazine = magazine  # goes through property setter

        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be string 5–50 chars")
        self._title = title

        # Add each new article to the class-level list
        Article.all.append(self)

    # ----- Properties -----
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # Ignore attempts to reset title
        pass

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an Author instance")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be a Magazine instance")
        self._magazine = value


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

    # ----- Required methods -----
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
    all = []  # track all magazines

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Name must be a string 2–16 chars")
        if not isinstance(category, str) or not (len(category) > 0):
            raise Exception("Category must be a non-empty string")

        self._name = name
        self._category = category
        Magazine.all.append(self)

    # ----- Properties -----
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    # ----- Relationships -----
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles or None

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        counts = Counter(authors)
        result = [author for author, count in counts.items() if count > 2]
        return result or None

    # ----- Bonus -----
    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        return max(cls.all, key=lambda mag: len(mag.articles()))
