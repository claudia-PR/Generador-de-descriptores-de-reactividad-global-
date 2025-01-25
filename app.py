streamlit run app.py
import streamlit as st
from rdkit import Chem
from rdkit.Chem import Descriptors

# Título de la aplicación
st.title("Generador de Descriptores de Reactividad Global")
st.markdown(
    """
    Esta aplicación calcula descriptores de reactividad global a partir de las energías HOMO y LUMO.
    **Instrucciones**:
    1. Ingresa una molécula en formato SMILES.
    2. Proporciona las energías HOMO y LUMO.
    3. Obtendrás valores como:
       - Afinidad electrónica
       - Energía de ionización
       - Dureza global
       - Electronegatividad
    """
)

# Entrada: SMILES
smiles = st.text_input("Introduce el SMILES de la molécula", value="")

if smiles:
    try:
        # Validar SMILES
        mol = Chem.MolFromSmiles(smiles)
        if mol:
            st.success("El SMILES ingresado es válido.")
            st.write("Molécula:", Chem.MolToMolBlock(mol), unsafe_allow_html=True)
        else:
            st.error("El SMILES ingresado no es válido.")
    except Exception as e:
        st.error(f"Error procesando el SMILES: {e}")

# Entrada: Energías HOMO y LUMO
homo = st.number_input("Introduce la energía HOMO (eV):", value=0.0, format="%.4f")
lumo = st.number_input("Introduce la energía LUMO (eV):", value=0.0, format="%.4f")

# Calcular los descriptores
if st.button("Calcular descriptores"):
    try:
        # Descriptores de reactividad global
        energia_ionizacion = -homo  # Aproximación
        afinidad_electronica = -lumo
        dureza_global = (lumo - homo) / 2
        electronegatividad = -(homo + lumo) / 2

        # Mostrar resultados
        st.subheader("Resultados")
        st.write(f"**Energía de ionización (eV):** {energia_ionizacion:.4f}")
        st.write(f"**Afinidad electrónica (eV):** {afinidad_electronica:.4f}")
        st.write(f"**Dureza global (eV):** {dureza_global:.4f}")
        st.write(f"**Electronegatividad (eV):** {electronegatividad:.4f}")

    except Exception as e:
        st.error(f"Error en el cálculo: {e}")
