# # 데이터관리에는 orm 사용 자제, 오버헤드때문에 게속 속도가 느려짐.
# orm은 프로그래밍 테크닉 sqlqlchemy, diango 등의 종류가 있음



import sqlalchemy

sqlalchemy.__version__

!pip install sqlalchemy

from sqlalchemy.engine import create_engine
from sqlalchemy.schema import Table, Column, ForeignKey
from sqlalchemy.types import Integer, Text
from sqlalchemy.sql import select, insert, update

from sqlalchemy.schema import MetaData

from sqlalchemy.schema import ForeignKey

from sqlalchemy.sql import or_, and_

from sqlalchemy.sql import join

!dir *.db

engine = create_engine('sqlite:///playlist.db', echo=True)

conn = engine.connect()



meta = MetaData()

meta.reflect(conn)

len(meta.tables), meta.tables.keys()

meta.tables['TRACK'].c.keys()

Artist = meta.tables['ARTIST']
Album = meta.tables['ALBUM']
Genre = meta.tables['GENRE']
Track = meta.tables['TRACK']

print(Artist.select())
conn.execute(Artist.select()).fetchall()

print(Album.join(Artist, Album.c.FK==Artist.c.PK))

conn.execute(select(*[Artist.c.NAME, Album.c.NAME]).select_from(
    Album.join(Artist, Album.c.FK==Artist.c.PK)
)).fetchall()

print(Album.join(Artist, Album.c.FK==Artist.c.PK).join(Track, Track.c.AFK==Album.c.PK))



conn.execute(select(*[Artist.c.NAME, Album.c.NAME, Track.c.NAME]).select_from(
    Album.join(Artist, Album.c.FK==Artist.c.PK).join(Track, Track.c.AFK==Album.c.PK)
)).fetchall()

print(Album.join(Artist, Album.c.FK==Artist.c.PK)\
      .join(Track, Track.c.AFK==Album.c.PK)\
      .join(Genre, Track.c.GFK==Genre.c.PK))

conn.execute(select(*[Artist.c.NAME, Album.c.NAME, Genre.c.NAME, Track.c.NAME])\
             .select_from(
    Album.join(Artist, Album.c.FK==Artist.c.PK)\
      .join(Track, Track.c.AFK==Album.c.PK)\
      .join(Genre, Track.c.GFK==Genre.c.PK)
)).fetchall()

Artist

meta.clear()
conn.close()

engine = create_engine('sqlite:///:memory:', echo=True)
conn = engine.connect()

meta

Table('TEMP', meta, Column('PK', Integer))

Table('TEMP', meta, Column('PK', Integer, primary_key=True), extend_existing=True)

Table('TEMP', meta, Column('PK', Integer, primary_key=True),
      Column('NAME', Text), extend_existing=True)

meta.create_all(conn)

Table('TEMP', meta, Column('PK', Integer, primary_key=True),
      Column('NAME', Text),
      Column('FK', Integer),
      extend_existing=True)

meta.create_all(conn)



