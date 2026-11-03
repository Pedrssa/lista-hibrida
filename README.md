# Atlas da Lista Híbrida

Simulador acadêmico de estruturas de dados em **Python + Streamlit**, com identidade visual Dark Academia × Celestial Vintage × Esotérico Antigo. Este repositório contém exclusivamente a Lista Híbrida; a Cifra de César permanece no seu repositório original.

## Funcionalidades
- Geração determinística de 1.024 inteiros distintos por semente fixa.
- Cauda de até 10 chaves, preservando a ordem de inserção e recusando duplicatas.
- Busca binária na parte ordenada e busca sequencial na cauda.
- Contagem de iterações, comparações, região e posição.
- Mesclagem ordenada na décima inserção válida, com cauda reutilizável.
- Interface responsiva, tema editorial e testes automatizados.

## Execução local

Requer Python 3.11 ou superior.

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

## Testes

```bash
python -m unittest discover -s tests -v
python -m py_compile app.py estrutura.py tema.py
```

## Publicação no Streamlit Community Cloud

Acesse https://share.streamlit.io/, escolha o repositório `Pedrssa/lista-hibrida`, branch `main`, e configure **Main file path** como `app.py`. Confira a URL pública e os principais fluxos antes de apresentar.

## Convenção das métricas

Uma iteração corresponde a uma passagem de laço. Na busca binária, igualdade e ordenação são comparações distintas. Na sequencial, cada chave examinada representa uma comparação. Os índices começam em zero em cada região.

## Entrega

**Antes de entregar:** publicar no Streamlit Cloud, conferir desktop/celular e demonstrar inserção, duplicatas, buscas e mesclagem.

## Integrantes
- Ricardo Henrique Rocha Silva
- Pedro Henrique Martins Mattos Paranhos Barreiros
- Brunno Otavyo De Jesus Aguiar
- Murilo Ribeiro
- Luis Eduardo Barbosa de Menezes Junior O pipeline de testes não substitui validação visual.
