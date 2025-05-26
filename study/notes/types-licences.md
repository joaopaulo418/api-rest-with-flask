# Licenças de Software para Projetos Git

Este documento apresenta um resumo completo das principais licenças de software utilizadas em projetos com controle de versão via Git. As licenças são classificadas por tipo (permissivas, copyleft, etc.) e incluem suas principais características e aplicações.

---

## 📄 Tipos de Licença

### 1. **Permissivas**
Permitem uso, modificação e redistribuição, inclusive em software fechado, desde que sejam mantidos os avisos de copyright.

- **MIT License**
  - Muito simples e flexível.
  - Pode usar, modificar, sublicenciar e distribuir.
  - Basta manter o aviso de copyright e isenção de responsabilidade.
  - Usada em: React, Ruby on Rails, Node.js.

- **BSD License (2 e 3 Cláusulas)**
  - Similar à MIT, com uma cláusula extra que proíbe uso do nome do autor para promoção.
  - Pode ser usada em software fechado.
  - Usada em: FreeBSD, partes do macOS e Windows.

- **Apache License 2.0**
  - Permissiva com proteção de patentes.
  - Requer aviso de modificações e inclui termos sobre patentes.
  - Usada em: Android, Hadoop, projetos Apache.

- **Unlicense / CC0**
  - Libera o código para domínio público.
  - Nenhuma restrição, nem mesmo atribuição.
  - Usada por quem deseja abandonar totalmente direitos sobre o código.

---

### 2. **Copyleft (Restritivas)**
Exigem que códigos derivados sejam distribuídos sob a mesma licença.

- **GPL (GNU General Public License)**
  - Forte copyleft: se derivado, também deve ser GPL.
  - Requer distribuição de código-fonte.
  - Usada em: Linux, WordPress, GCC.

- **LGPL (Lesser GPL)**
  - Copyleft moderado: permite uso em software fechado, desde que não modifique a biblioteca.
  - Usada em: GTK, FFMpeg.

- **AGPL (Affero GPL)**
  - Mais restritiva que a GPL: requer abertura mesmo se o software for apenas executado remotamente.
  - Usada em: sistemas web que prezam por transparência de código.

- **MPL (Mozilla Public License)**
  - Copyleft leve: apenas arquivos modificados devem ser abertos.
  - Pode ser usada com partes fechadas.
  - Usada em: Firefox, Thunderbird.

---

### 3. **Creative Commons (CC)**
Não são apropriadas para código, mas úteis para documentação, textos e mídia.

- **CC BY**: Usa livremente, desde que cite o autor.
- **CC BY-SA**: Mesmo que CC BY, mas derivados também devem ter a mesma licença.
- **CC0**: Equivalente ao domínio público.
- **CC BY-NC**: Proíbe uso comercial.

---

## 🔹 Comparativo Rápido

| Licença      | Permissiva | Uso comercial | Copyleft | Código fechado permitido | Proteção de patente |
|--------------|------------|----------------|----------|----------------------------|-----------------------|
| MIT          | Sim        | Sim            | Não      | Sim                        | Não                  |
| BSD          | Sim        | Sim            | Não      | Sim                        | Não                  |
| Apache 2.0   | Sim        | Sim            | Não      | Sim                        | Sim                  |
| GPL          | Não       | Sim            | Sim      | Não                       | Não                  |
| LGPL         | Parcial    | Sim            | Sim      | Sim (com restrição)      | Não                  |
| AGPL         | Não       | Sim            | Sim      | Não                       | Não                  |
| MPL          | Parcial    | Sim            | Leve     | Sim                        | Não                  |
| Unlicense    | Sim        | Sim            | Não      | Sim                        | Não                  |
| CC (varia)   | Depende    | Depende        | Depende  | Depende                    | Não                  |

---

## 📁 Sugestões de Uso por Objetivo

| Objetivo                                               | Licença sugerida        |
|--------------------------------------------------------|--------------------------|
| Quero que todos usem livremente, sem restrições       | MIT, BSD, Unlicense     |
| Quero evitar uso comercial ou fechado                  | GPL, AGPL               |
| Quero proteger contra processos de patente             | Apache 2.0              |
| Quero liberar biblioteca para qualquer tipo de uso     | LGPL, MPL               |
| Estou distribuindo conteúdo (documentos, imagens)      | Creative Commons (CC)   |