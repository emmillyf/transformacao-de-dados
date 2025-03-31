<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>📁 Teste de Transformação de Dados</h1>
    
  <p>Este projeto realiza a extração, transformação e compactação de dados de um arquivo PDF (<strong>Anexo I</strong>) contendo a <strong>Tabela Rol de Procedimentos e Eventos em Saúde</strong>, seguindo os requisitos do teste técnico.</p>

  <h2>📋 Requisitos</h2>
    <ul class="checklist">
        <li>Extrair tabelas de um PDF (todas as páginas)</li>
        <li>Renomear colunas</li>
        <li>Salvar em CSV estruturado</li>
        <li>Compactar o CSV em um arquivo ZIP</li>
    </ul>

  <h2>⚙️ Tecnologias Utilizadas</h2>
    <ul>
        <li><strong>Python 3.10+</strong></li>
        <li>Bibliotecas:
            <ul>
                <li><code>Pdfplumber</code> (extração de tabelas de PDF)</li>
                <li><code>pandas</code> (manipulação de dados em DataFrame)</li>
                <li><code>Zipfile</code> (compactação do CSV em ZIP)</li>
            </ul>
        </li>
    </ul>

 <h3>📦 Dependências</h3>
<pre><code>pip install pandas pdfplumber</code></pre>
<p>Ou instale a partir do arquivo de requisitos:</p>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>📖 Como Executar</h3>
    <ol>
        <li><strong>Clone o repositório:</strong></li>
      <pre><code>git clone https://github.com/emmillyf/transformacao-de-dados.git
</code></pre>
        <li><strong>Instale as dependências:</strong></li>
        <pre><code>pip install -r requirements.txt</code></pre>
        <li><strong>Execute o script:</strong></li>
        <pre><code>python scripts/main.py</code></pre>
    </ol>

  <h3>3️⃣ Saída Esperada</h3>
    <ul>
        <li><strong><code>Anexo_I_Completo.csv</code></strong> (tabela extraída em CSV)</li>
        <li><strong><code>Teste_{Nome}.zip</code></strong> (CSV compactado)</li>
    </ul>

  <div class="note">
        <h3>📌 Observações</h3>
        <ol>
            <li><strong>Ao abrir o CSV no Excel</strong>:
                <ul>
                    <li>Selecione todas as colunas</li>
                    <li>Vá em <strong>Formatar</strong> → <strong>AutoAjuste Largura da Coluna</strong></li>
                    <li>Isso garantirá que todo o texto seja exibido corretamente, sem cortes</li>
                </ul>
            </li>
        </ol>
    </div>
    <hr>
<p>Feito por <strong>Emmilly Gomes</strong></p>
</body>
