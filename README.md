# Footprint

This is just a graph-generator script for git repos to give *one* view of
contributor footprint. It fundamentally counts `git blame` lines, so the
perspective is with emphasis on who last worked on the code rather than other
types of contribution.

We count lines with `git blame -w -C -C -C` where `-w` ignores white-space and
`-C -C -C` detects lines moved or copied in any commit so that it does not
'give credit' for e.g. a moved function.
 
<img src="labwc.png"/><br/>

Footprint also supports a shell-plot:

```bash
CACHE_DIR=.cache/wlroots ./plot.py --shell-plot --tags "$(find .cache/wlroots -type f -printf "%f ")"
```

```
  Author                    0.10.0 0.11.0 0.12.0 0.13.0 0.14.0 0.15.0 0.16.0 0.16.2 0.17.0 0.17.4 0.18.0 0.18.2
  ------------------------- ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------
  emersion                   25441  27689  26763  29889  30552  34030  34683  34805  41006  41046  43031  43074
  Drew DeVault               11728  11655  11563  11452  11400  11001  10484  10481   9143   9138   8823   8826
  Tony Crisci                 7116   7051   5771   5689   5642   5535   5095   5089   4743   4738   4683   4676
  Alexander Orzechowski          0      0      0      0      0      0   1921   1923   3984   3979   4317   4336
  Kirill Primak                  0      0      0      0      0    537   2422   2427   3089   3157   3573   3579
  Simon Zeni                     0     47     47    239   1143   2552   3914   3918   3705   3697   3452   3452
  Markus Ongyerth             4708   4846   4823   4712   4704   4649   4174   4174   3342   3342   3312   3312
  nyorain                      904    914    912    803    675   4214   3472   3472   2890   2888   2560   2560
  Scott Anderson              4792   4893   4886   4220   3181   2973   2756   2755   2521   2519   2400   2396
  Ilia Bozhinov               1511   1520   1681   2720   2651   2628   2433   2433   1995   2030   2064   2065
  Manuel Stoeckl               208    236    235    265    260    423    432    432   1046   1045   1762   1762
  Dorota Czaplejewicz         2143   2258   2266   2275   2275   2286   2203   2203   1490   1491   1503   1503
  Isaac Freund                   0    182    216    390    383    662   1499   1498   1401   1411   1464   1488
  Dominique Martinet          1916   1830   1775   1746   1727   1652   1222   1222   1111   1105   1081   1081
  Guido Günther                835   1183   1174   1160   1063   1199   1251   1252   1043   1047   1043   1044
  Timidger                    1065   1058   1059   1055   1101   1084   1022   1022    770    770    766    766
  Kenny Levinsen                 0     26    231    324    250    247    514    514    715    720    749    750
  Greg V                       794    788    789    786    714    819    651    651    650    650    647    647
  Tudor Brindus                  0    161    257    564    636    641    636    636    620    620    612    612
  Andri Yngvason               231    742    728    732    650    632    564    565    420    420    570    570
  Las                          571    575    577    591    591    580    574    574    457    461    464    464
  Rose Hudson                    0      0      0      0      0      0      0      0    411    411    402    402
  Josef Gajdusek               542    544    542    542    542    541    487    487    392    392    392    392
  Brian Ashworth               465    529    491    476    470    441    402    402    390    390    389    387
  Ivan Molodetskikh            350    341    341    341    341    327    327    327    319    319    317    317
  random human                 777    789    790    769    767    723    683    683    276    273    271    271
  Michael Weiser                 0    324    324    338    338    338    336    336    260    260    259    259
  David96                        0     13     13     13     13     13    258    251    257    257    255    254
  columbarius                    0      0      0      0      0      0      0      0      0      0    221    227
  vaxerski                       0      0      0      0      0      0      2      2    225    225    218    218
  Tadeo Kondrak                  0      0      0     14    130    274    255    255    210    212    211    211
  xdavidwu                       1    308    310    310    312    312    306    306    201    201    201    201
  Daniel Kondor                  0      0    115    238    238    237    233    233    179    179    179    179
  José Expósito                  0      0      0      0      0    118    201    201    190    190    178    178
  Sebastian Krzyszkowiak       222    222    181    180    180    178    158    158    155    155    160    160
```

