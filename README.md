# Projectile Motion Analysis

This repository contains a Python script designed to analyze projectile motion data from a classic physics experiment: a sphere rolling down a ramp and launching horizontally from a table. The script compares experimental data with two theoretical models—**Point Mass** and **Rigid Body**—to determine which provides a more accurate description of reality.

It is designed for high school and university physics students, teachers, and researchers. **No prior knowledge of Python is required to use this tool.**

---

## English

### 1. Overview

This project provides a simple yet powerful tool for analyzing the results of a projectile motion experiment. By inputting your experimental data—specifically, the release heights on a ramp and the resulting horizontal ranges—the script will:

1.  **Plot your data** against the theoretical predictions.
2.  Perform a **linear regression** to find the best-fit line for your measurements.
3.  Calculate the **theoretical results** based on two distinct physical models.
4.  Quantify the **percentage error** between your data and each model.
5.  Generate a high-quality graph and a console report summarizing the findings.

### 2. The Physics Behind It: Point Mass vs. Rigid Body

When a sphere rolls down a ramp, its potential energy is converted into kinetic energy. However, this kinetic energy has two components: **translational** (moving forward) and **rotational** (spinning).

-   **Model 1: Point Mass**
    This is the simplest model. It assumes the sphere is a single point and **ignores rotational energy**. All the initial potential energy is converted into translational kinetic energy. This model predicts a higher launch velocity.

-   **Model 2: Rigid Body**
    This model is more realistic. It treats the sphere as a rigid body that both slides and spins. Part of the potential energy becomes rotational kinetic energy, leaving less for translational motion. This model predicts a slightly lower launch velocity than the Point Mass model.

The goal of the experiment is to see which model's predictions align better with real-world measurements.

### 3. How to Use This Tool

You only need to edit the `projectile-analysis.py` file in three specific places.

**Step 1: Set the Table Height (`h0`)**

Find this line and replace `0.85` with the height of your table or ramp in **meters**.
```python
# Experiment parameters (INSERT YOUR VALUES HERE)
h0 = 0.85  # Height of the table/ramp (m). Example: 85 cm = 0.85 m
```

**Step 2: Enter Your Release Heights (`h_exp`)**

Find this section and replace the example values inside the square brackets `[]` with your own release heights from the ramp, also in **meters**.
```python
# Insert the values of 'h' (launch height on the ramp) in meters
h_exp = np.array([
    0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.16, 0.18, 0.20
])
```

**Step 3: Enter Your Measured Ranges (`A_exp`)**

Finally, find this line and replace `A_exp_example` with an array of your own measured horizontal ranges in **meters**. The number of range values must match the number of height values.
```python
# INSERT YOUR REAL RANGE DATA 'A' HERE:
# Example: A_exp = np.array([0.15, 0.21, 0.26, ...])
A_exp = A_exp_example  # <- REPLACE "A_exp_example" WITH YOUR DATA
```
For example, if your measured ranges were 15 cm, 21 cm, etc., you would write:
```python
A_exp = np.array([0.15, 0.21, 0.26, 0.30, 0.33, 0.36, 0.39, 0.41, 0.43, 0.45])
```

**Step 4: Run the Script**

Save the file and run it from your terminal using:
```bash
python projectile-analysis.py
```

### 4. Understanding the Output

The script generates two outputs:

-   **A graph (`result.png`):** This visualizes your experimental data (black dots) against the theoretical lines for the Point Mass (blue dashed) and Rigid Body (red solid) models. It also shows the best-fit line from your data (green dotted).
-   **A console report:** This text output provides a quantitative analysis, including:
    -   The theoretical slopes calculated for each model.
    -   The experimental slope from your data.
    -   The percentage error between your results and each model, making it easy to see which one is a better fit.

---

## Português

### 1. Visão Geral

Este repositório contém um script Python projetado para analisar dados de movimento de projéteis de um experimento clássico de física: uma esfera rolando por uma rampa e sendo lançada horizontalmente de uma mesa. O script compara os dados experimentais com dois modelos teóricos — **Ponto Material** e **Corpo Rígido** — para determinar qual deles descreve a realidade com mais precisão.

Ele foi desenvolvido para estudantes de ensino médio e universitário, professores de física e pesquisadores. **Nenhum conhecimento prévio de Python é necessário para usar esta ferramenta.**

### 2. A Física por Trás do Experimento: Ponto Material vs. Corpo Rígido

Quando uma esfera rola por uma rampa, sua energia potencial é convertida em energia cinética. No entanto, essa energia cinética possui dois componentes: **translacional** (o movimento para a frente) e **rotacional** (o giro).

-   **Modelo 1: Ponto Material**
    Este é o modelo mais simples. Ele assume que a esfera é um único ponto e **ignora a energia de rotação**. Toda a energia potencial inicial é convertida em energia cinética translacional. Este modelo prevê uma velocidade de lançamento maior.

-   **Modelo 2: Corpo Rígido**
    Este modelo é mais realista. Ele trata a esfera como um corpo rígido que, ao mesmo tempo, desliza e gira. Parte da energia potencial se torna energia cinética de rotação, deixando menos energia para o movimento de translação. Este modelo prevê uma velocidade de lançamento ligeiramente menor que a do Ponto Material.

O objetivo do experimento é verificar qual dos modelos teóricos se alinha melhor com as medições do mundo real.

### 3. Como Usar a Ferramenta

Você só precisa editar o arquivo `projectile-analysis.py` em três lugares específicos.

**Passo 1: Defina a Altura da Mesa (`h0`)**

Encontre esta linha e substitua `0.85` pela altura da sua mesa ou rampa em **metros**.
```python
# Experiment parameters (INSERT YOUR VALUES HERE)
h0 = 0.85  # Height of the table/ramp (m). Example: 85 cm = 0.85 m
```

**Passo 2: Insira Suas Alturas de Lançamento (`h_exp`)**

Encontre esta seção e substitua os valores de exemplo dentro dos colchetes `[]` pelas suas próprias alturas de lançamento na rampa, também em **metros**.
```python
# Insert the values of 'h' (launch height on the ramp) in meters
h_exp = np.array([
    0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.16, 0.18, 0.20
])
```

**Passo 3: Insira Seus Alcances Medidos (`A_exp`)**

Finalmente, encontre esta linha e substitua `A_exp_example` por um array com os seus próprios alcances horizontais medidos em **metros**. O número de valores de alcance deve ser igual ao número de valores de altura.
```python
# INSERT YOUR REAL RANGE DATA 'A' HERE:
# Example: A_exp = np.array([0.15, 0.21, 0.26, ...])
A_exp = A_exp_example  # <- REPLACE "A_exp_example" WITH YOUR DATA
```
Por exemplo, se seus alcances medidos foram 15 cm, 21 cm, etc., você escreveria:
```python
A_exp = np.array([0.15, 0.21, 0.26, 0.30, 0.33, 0.36, 0.39, 0.41, 0.43, 0.45])
```

**Passo 4: Execute o Script**

Salve o arquivo e execute-o a partir do seu terminal usando:
```bash
python projectile-analysis.py
```

### 4. Entendendo os Resultados

O script gera dois resultados:

-   **Um gráfico (`result.png`):** Ele visualiza seus dados experimentais (pontos pretos) em comparação com as linhas teóricas dos modelos de Ponto Material (azul tracejada) e Corpo Rígido (vermelha sólida). Ele também mostra a linha de melhor ajuste (regressão linear) para os seus dados (verde pontilhada).
-   **Um relatório no console:** Este texto exibe uma análise quantitativa, incluindo:
    -   As inclinações teóricas calculadas para cada modelo.
    -   A inclinação experimental obtida a partir dos seus dados.
    -   O erro percentual entre seus resultados e cada modelo, facilitando a identificação de qual deles se ajusta melhor.
