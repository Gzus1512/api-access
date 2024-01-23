from datetime import datetime
from typing import Optional

from sqlalchemy import create_engine, func, select, insert
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
from sqlalchemy.types import DateTime, Integer, String


class Base(DeclarativeBase):
    pass


class Cards(Base):
    __tablename__ = "cat_tarjeta"

    cat_tarjeta_id: Mapped[int] = mapped_column(Integer(), primary_key=True, nullable=False)
    cat_locatario_id: Mapped[int] = mapped_column(Integer())
    numero_tarjeta: Mapped[str] = mapped_column(String(32))
    codigo_tarjeta: Mapped[str] = mapped_column(String(16))
    estado_tarjeta: Mapped[int] = mapped_column(Integer())

    def __repr__(self) -> str:
        return (
            f"Card(id={self.cat_tarjeta_id!r}, "
            f"owner={self.cat_locatario_id!r}, "
            f"code={self.codigo_tarjeta!r})"
        )


class Logs(Base):
    __tablename__ = "tbl_log_tarjeta"

    tbl_log_rfid_id: Mapped[int] = mapped_column(Integer(), primary_key=True, nullable=False)
    cat_dispositivo_rfid_id: Mapped[int] = mapped_column(Integer(), nullable=False)
    cat_tarjeta_id: Mapped[int] = mapped_column(Integer(), nullable=False)
    cat_evento_tarjeta_id: Mapped[int] = mapped_column(Integer())
    fecha_hora: Mapped[datetime] = mapped_column(DateTime())
    imagen: Mapped[str] = mapped_column(String(128))

    def __repr__(self) -> str:
        return (
            f"Log(id={self.tbl_log_rfid_id!r}, "
            f"evento={self.cat_evento_tarjeta_id!r}, "
            f"date={self.fecha_hora!r})"
        )
    
class User(Base):
    __tablename__ = "test_users"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))

def main() -> None:
    """ number_of_logs = int(
        input("How many top customers do you want to query? ")
    ) """

    engine = create_engine("mysql+pymysql://root:@localhost:3306/control_access")
    session = Session(engine)

    newUser = User(
        name = "Jesus",
        email = "jr@mail.com",
        password = "absdfgh123456"
    )

    session.add(newUser)
    session.commit()
    """ stmt = (
        select(
            Cards.cat_tarjeta_id,
            Cards.codigo_tarjeta,
            func.sum(Logs.cat_dispositivo_rfid_id).label("Total")
        )
        .join(Logs, Cards.cat_tarjeta_id == Logs.cat_tarjeta_id)
        .group_by(Cards.cat_tarjeta_id)
        .order_by(func.sum(Logs.cat_dispositivo_rfid_id).label("Total").desc())
        .limit(number_of_logs)
    )

    for card in session.execute(stmt):
        print(card) """


if __name__ == "__main__":
    main()