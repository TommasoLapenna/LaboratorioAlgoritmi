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