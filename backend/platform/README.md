Один ко многим с обратной связью много к одному
это только в роидетльском List[] и back_population

Один к одному - без List и там и там

Много ко многим делается через ассоциативную таблицу
association_table = Table(
    "association_table",
    Base.metadata,
    Column("left_id", ForeignKey("left_table.id")),
    Column("right_id", ForeignKey("right_table.id")),
)
children: Mapped[List[Child]] = relationship(
        secondary=association_table, back_populates="parents"
    )
parents: Mapped[List[Parent]] = relationship(
        secondary=association_table, back_populates="children"
    )