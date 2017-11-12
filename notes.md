# overlap számítás
bináris számként ábrázoljuk a címeket és maszkokat
addr & mask -> ez a szám lesz a networkID
networkID-hoz hozzáadunk egyet -> ez a legkisebb host address
networkID & (~mask) -> broadcast address
broadcast address - 1 -> ez a legnagyobb host address
sorbarendezzük a range-eket a legkisebbek szerint
nézzük a legkisebbtől, hogy overlap van-e

# useful
https://docs.python.org/3/library/ipaddress.html
https://docs.python.org/3/howto/ipaddress.html

# TODO
- test addressess for overlapping
- separate regexps, add expression for ipv6 too