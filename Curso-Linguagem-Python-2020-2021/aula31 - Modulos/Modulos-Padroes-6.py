"""
 * MÓDULOS PADRÕES

   - O Python traz uma biblioteca padrão de módulos, descrita em um documento em separado, a Referência da Biblioteca Python (doravante “Referência da Biblioteca”). Alguns módulos estão embutidos no interpretador; estes possibilitam acesso a operações que não são parte do núcleo da linguagem, mas estão no interpretador seja por eficiência ou para permitir o acesso a chamadas do sistema operacional. O conjunto destes módulos é uma opção de configuração que depende também da plataforma utilizada. Por exemplo, o módulo winreg só está disponível em sistemas Windows. Existe um módulo que requer especial atenção: sys, que é embutido em qualquer interpretador Python. As variáveis sys.ps1 e sys.ps2 definem as strings utilizadas como prompt primário e secundário:

"""

import sys

print("PROMPT PRIMARIO DEFINIDO: " + sys.ps1)

print("PROMPT SECUNDARIO DEFINIDO: " +  sys.ps2)

"""
 - Essas variáveis só estão definidas se o interpretador está em modo interativo.

"""