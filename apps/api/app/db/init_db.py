from app.db.session import create_all


def init_db() -> None:
    create_all()


if __name__ == "__main__":
    init_db()
    print("DB schema created")
