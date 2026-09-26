## Notes
La relazione deve contenere: 
- **Intro**
- **Desc teorica degli algoritmi**
  - Riassunto, no dimostrazioni
- **Prestazioni attese**
- **Esperimenti**
  - Dati utilizzati e fonti
  - Specifiche HW/SW
  - Misurazioni effettuate (tipo, quantità di test)
- **Documentazione del codice**
  - Schema del contenuto e interazioni fra moduli
  - Schema delle classi
  - Analisi delle alternative implementate
  - Metodi implementati (I/O)
- **Risultati (tabelle e grafici)**
  - Tabelle contenti tutti i dati
  - Cifre significative appropriate
  - Didascalia
  - Dati citati nel testo (\label{}, \red{})
- **Analisi completa sui risultati**
  - Risultati commentati e analizzati
  - Verifica delle ipotesi teoriche
  - Paragrafo di conclusione per la sintesi dei dati

```
\documentclass[]{article}
\begin{document}
 Hello World!
\end{document}
```

Vogliamo confrontare varie implementazioni di statistiche d'ordine dinamiche:
1    Con lista ordinata
2    Con ABR senza attributo {\em size}
3    Come visto a lezione

Nota: La lista deve essere implementata considerando strutture collegate con puntatori e non la struttura dati lista di Python.

---

- Linked list:
  - LinkedList() empty list
  - LinkedList(node) starting node
  - search(node) search node
  - delete(node) delete node
  - orderedInsert(node)
- Node
  - Node(next, key)

- Binary Tree:
  - InOrderTreeWalk() print
  - treeMinium/treeMaximum(node) maximum and minimun from a starting node
  - iterativeSearch(node) iterative search of a node
  - treeInsert(node) insert new node
  - treeDelete(node) delete a node


RESULTS

Linked List

| n     | os select time | os select nodes | os rank time | os rank nodes |
|-------|----------------|-----------------|--------------|---------------|
| 10    | 0.47           | 6.61            | 0.52         | 7.19          |
| 20    | 0.71           | 11.79           | 0.81         | 12.94         |
| 50    | 1.40           | 27.97           | 2.11         | 28.77         |
| 100   | 3.25           | 60.75           | 4.02         | 60.45         |
| 200   | 6.37           | 129.39          | 7.25         | 129.11        |
| 500   | 35.56          | 366.20          | 42.42        | 365.86        |
| 1000  | 54.36          | 649.10          | 73.00        | 658.84        |
| 2000  | 123.62         | 1271.41         | 134.60       | 1271.15       |
| 5000  | 269.49         | 3245.37         | 345.50       | 3245.06       |
| 10000 | 431.55         | 6689.20         | 493.57       | 6688.89       |



Order Statistics Tree

| n     | os select time | os select nodes | os rank time | os rank nodes |
|-------|----------------|-----------------|--------------|---------------|
| 10    | 1.05           | 7.16            | 1.18         | 7.96          |
| 20    | 1.80           | 12.82           | 2.70         | 14.22         |
| 50    | 4.05           | 29.42           | 4.38         | 30.42         |
| 100   | 9.87           | 63.34           | 10.48        | 63.34         |
| 200   | 17.43          | 131.48          | 22.94        | 131.48        |
| 500   | 64.97          | 368.87          | 81.62        | 368.87        |
| 1000  | 128.53         | 653.02          | 138.68       | 663.02        |
| 2000  | 282.00         | 1275.40         | 291.91       | 1275.40       |
| 5000  | 601.07         | 3249.68         | 615.83       | 3249.68       |
| 10000 | 1222.16        | 6694.06         | 1209.56      | 6694.06       |

Augmented AVL Tree


| n     | os select time | os select nodes | os rank time | os rank nodes |
|-------|----------------|-----------------|--------------|---------------|
| 10    | 0.57           | 2.71            | 0.49         | 2.71          |
| 20    | 2.30           | 3.81            | 1.58         | 3.88          |
| 50    | 0.86           | 4.96            | 0.69         | 4.94          |
| 100   | 1.13           | 6.23            | 0.87         | 6.23          |
| 200   | 1.22           | 7.0             | 0.93         | 7.0           |
| 500   | 1.70           | 8.24            | 2.59         | 8.24          |
| 1000  | 1.77           | 9.31            | 1.74         | 9.31          |
| 2000  | 3.52           | 10.69           | 5.16         | 10.69         |
| 5000  | 3.39           | 11.67           | 3.63         | 11.67         |
| 10000 | 2.69           | 12.61           | 1.78         | 12.61         |

Tempi in µs, nodi visitati = media su 100 query. Grafici in `grafici.tex`.

Correzioni ai dati (errori di trascrizione):
- ABR, n=2000, OS-SELECT nodi: 1271.15 → 1275.40 (era il valore di OS-RANK della lista;
  nell'ABR OS-SELECT e OS-RANK visitano gli stessi nodi, salvo query con i=0)
- AVL, n=2000, OS-RANK nodi: 20.69 → 10.69 (identico a OS-SELECT in tutte le altre righe)


COMMENTO DEI RISULTATI

**Distribuzione delle query.** Il rango i è estratto uniformemente in [0, 4n/3], quindi
circa il 25% delle query è fuori intervallo (caso peggiore per lista e ABR: si visita
tutta la struttura). Il numero medio di nodi atteso per la lista è quindi
(n²/2 + n·n/3) / (4n/3) = 5n/8 ≈ 0.625n.

**Lista ordinata.** Crescita lineare, come atteso da Θ(i): i nodi visitati sono
≈ 0.63–0.67n (es. 6689 per n=10000), in accordo con la stima 5n/8 (lo scarto è dovuto
alla varianza su sole 100 query). Il tempo per nodo è ≈ 0.06–0.10 µs. OS-RANK è
leggermente più lento di OS-SELECT (493 vs 432 µs a n=10000) perché ad ogni nodo
confronta la chiave invece di decrementare un contatore.

**ABR senza size.** Asintoticamente identico alla lista: la visita in-order deve
contare tutti i nodi che precedono quello cercato, quindi è Θ(i). I nodi visitati sono
quelli della lista più un piccolo termine O(h) (i nodi rimasti sullo stack: da ≈2 a
n=100 a ≈5 a n=10000). In tempo però è ≈2.3–2.8 volte più lento della lista
(1222 vs 432 µs a n=10000) per il costo di push/pop sullo stack e dei puntatori in più.
Nell'ABR OS-SELECT e OS-RANK visitano esattamente gli stessi nodi; le differenze per
n piccolo (10, 20, 50, 1000) sono dovute alle query con i=0: OS-SELECT termina subito,
mentre OS-RANK cerca una chiave assente e visita tutti gli n nodi.

**AVL aumentato.** Crescita logaritmica: i nodi visitati aumentano di ≈3.3 ogni volta
che n si moltiplica per 10 (6.23 → 9.31 → 12.61), cioè esattamente log₂10, e restano
sempre poco sotto log₂n (12.61 contro 13.29 a n=10000), coerente con un albero
bilanciato di altezza ≤ 1.44·log₂n. I tempi (1–5 µs) sono vicini alla risoluzione
della misura e quindi rumorosi (es. il picco a n=20 o a n=2000), ma restano
sostanzialmente costanti al crescere di n. OS-RANK è di solito un po' più veloce di
OS-SELECT perché è iterativo, mentre OS-SELECT è ricorsivo (costo delle chiamate).

**Confronto.** A n=10000 l'AVL visita ≈530 volte meno nodi della lista (12.6 vs 6689)
ed è ≈160 volte più veloce (2.7 vs 432 µs), ≈450 volte rispetto all'ABR. Per n ≤ 20
le tre strutture sono confrontabili: il vantaggio asintotico si vede solo per n grandi.
Sul grafico log-log lista e ABR sono rette parallele di pendenza ≈1 (lineari), l'AVL è
quasi piatto.

**Conclusione.** Le ipotesi teoriche sono verificate: lista e ABR senza size hanno
costo Θ(n) per entrambe le operazioni, e l'ABR non porta alcun vantaggio (anzi è più
lento per le costanti). È l'attributo size, insieme al bilanciamento AVL, a ridurre il
costo a O(log n).


 


