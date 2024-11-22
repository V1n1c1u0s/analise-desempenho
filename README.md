# Repositório Para As Atividades Da Matéria Análise e Desempenho

## Atividade 1 e 2
<details>
<summary>C</summary>

```console
cd C && gcc -o main main.c
```

</details>
### Código em Python

```bash
cd python && python main.py
```

### Código em Java 
```sh
cd java/src && javac Main.java LinkedList.java && java Main
```
## Atividade 3 
Em andamento



<style>
/* Style the table to make it look neat */
.table-container {
  display: table;
  width: 100%;
  border-collapse: collapse;
}

.table-header {
  display: table-header-group;
}

.table-header div {
  display: inline-block;
  padding: 10px;
  background-color: #f0f0f0;
  border: 1px solid #ccc;
  cursor: pointer;
  text-align: center;
}

.table-content {
  display: table-row-group;
}

.table-content div {
  display: none;
  padding: 15px;
  border: 1px solid #ccc;
  background-color: #f9f9f9;
}

.table-content div.active {
  display: block;
}
</style>

<div class="table-container">
  <div class="table-header">
    <div onclick="showCode('python')">Python</div>
    <div onclick="showCode('java')">Java</div>
  </div>
  <div class="table-content">
    <div id="python" class="code-block">
      ```console
        cd python && python main.py
      ```
    </div>
    <div id="java" class="code-block">
      ```console
        cd java/src && javac Main.java LinkedList.java && java Main
      ```
    </div>
  </div>
</div>

<script>
// Function to show the correct code block
function showCode(language) {
  // Hide all code blocks
  const blocks = document.querySelectorAll('.code-block');
  blocks.forEach(block => block.classList.remove('active'));

  // Show the selected code block
  const selectedBlock = document.getElementById(language);
  selectedBlock.classList.add('active');
}
</script>
