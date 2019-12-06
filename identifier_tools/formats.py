import re

# List of national identifiers issued by European Central Bank
ECB_NATIONAL_IDENTIFIERS = {
    "AT_FB_CD": "^[0-9]{1,6}[A-Za-z][0-9]{0,3}?$",
    "AT_GEM_CD": "^[0-9]{5}$",
    "AT_IDENT_CD": "^[0-9]{1,8}$",
    "AT_LAE_CD": "^[0-9]$",
    "AT_ZVR_CD": "^[0-9]{1,10}$",
    "BE_OND_CD": "^0[0-9]{9}$",
    "BG_BULSTAT_CD": "(^[0-9]{9}$)|(^[0-9]{10}$)|(^[0-9]{13}$)",
    "BG_UIC_CD": "(^[0-9]{9}$)|(^[0-9]{13}$)$",
    "BG_VAT_CD": "^BG([0-9]{9}|[0-9]{10})$",
    "BIC": "(^[A-Z0-9]{8}$)|(^[A-Z0-9]{11}$)$",
    "BR_CNPJ_CD": "^[0-9]{2}[.][0-9]{3}[.][0-9]{3}/[0-9]{4}-[0-9]{2}$",
    "CA_BN_CD": "^[0-9]{9}$",
    "CH_ID_CD": "^CH[0-9]{11}$",
    "CH_NUMMER": "^CH-[0-9]{3}[.][0-9][.][0-9]{3}[.][0-9]{3}-[0-9]$",
    "CH_UID_CD": "^CHE-[0-9]{3}[.][0-9]{3}[.][0-9]{3}$",
    "CN_CC_CD": "^[A-Z0-9]{18}$",
    "CY_DRCOR_CD": "^[COP][0-9]{1,8}$",
    "CY_TIC_CD": "^[0-9]{8}[A-Z]$",
    "CY_IF_CD": "^CYIF[0-9]{4}$",
    "CY_PF_CD": "^PF[0-9]{1,4}$",
    "CY_GG_CD": "^S13[0-9]{8}$",
    "CY_VAT_CD": "^[013459][0-9]{7}[A-Z]$",
    "CY_CBCID_CD": "^[A-Z]{2}[0-9]{1,8}$",
    "CY_OTHER_CD": "^[^+,]{1,50}$",
    "CZ_ICO_CD": "^[0-9]{8}$",
    "CZ_NID_CD": "(^[0-9]{8}$)|(^[0-9]{10}$)",
    "DE_GNR_CD": "^G[nN]R[0-9]{1,6}[A-Z]{0,5}-[A-Z][0-9]{4}$",
    "DE_HRA_CD": "^HRA[0-9]{1,6}[A-Z]{0,5}-[A-Z][0-9]{4}$",
    "DE_HRB_CD": "^HRB[0-9]{1,6}[A-Z]{0,5}-[A-Z][0-9]{4}$",
    "DE_PR_CD": "^PR[0-9]{1,6}[A-Z]{0,5}-[A-Z][0-9]{4}$",
    "DE_VR_CD": "^VR[0-9]{1,6}[A-Z]{0,5}-[A-Z][0-9]{4}$",
    "DK_CVR_CD": "^[0-9]{8}$",
    "DK_FT_CD": "^[0-9]+-?[0-9]*$",
    "DK_SE_CD": "^[0-9]{8}$",
    "EE_FON_CD": "^[0-9]{1,4}$",
    "EE_RG_CD": "^[0-9]{8}$",
    "ES_NIF_CD": "^[A-Z0-9]{9}$",
    "FI_ALV_CD": "^FI[0-9]{8}$",
    "FI_SIRA_CD": "^[0-9]{8}#[0-9]{3}$",
    "FI_Y_CD": "^[0-9]{7}-?[0-9]$",
    "FR_CIB": "^[0-9]{5}$",
    "FR_RNA_CD": "^[A-Z][0-9]{9}$",
    "FR_SIREN_CD": "^[0-9]{9}$",
    "FR_IF_CD": "^FR[A-Z0-9]{10}$",
    "GB_VAT_CD": "^(GB([0-9]{9}|[0-9]{12})|GB(GD|HA)[0-9]{3})$",
    "GB_FSR_CD": "^[0-9]{6}$",
    "GB_CRN_CD": "^[A-Z0-9]{8}$",
    "GB_UTR_CD": "(^[0-9]{10}$)|(^[0-9]{9}K$)",
    "GR_AFM_CD": "^[0-9]{9}$",
    "GR_IMO_CD": "^[0-9]{7}$",
    "HK_BR_CD": "^[0-9]{8}-[0-9]{3}.[0-9]{2}.[0-9]{2}-[A-Z]$",
    "HK_CR_CD": "^[0-9]{7}$",
    "HR_MB_CD": "^[0-9]{8}$",
    "HR_MBS_CD": "^[01][0-9]{8}$",
    "HR_OIB_CD": "^[0-9]{11}$",
    "HU_CEG_CD": "^[0-9]{2}-[0-9]{2}-[0-9]{6}$",
    "HU_FB_CD": "^FB([0-9]{6}|[0-9]{3}[A-Z][0-9]{2})$",
    "HU_KOZ_CD": "^HU[0-9]{8}$",
    "HU_TOR_CD": "^[0-9]{8}$",
    "IE_CRO_CD": "^[1-9][0-9]{0,6}$",
    "IE_GOV_CD": "^(GV[0-9]{4}|LA[0-9]{3})$",
    "IN_CIN_CD": "^[A-Z0-9]{21}$",
    "IN_PAN_CD": "^[A-Z0-9]{10}$",
    "IT_ABI_CD": "^[^+,]{1,50}$",
    "IT_CCIAA_CD": "^[A-Z]{2}[0-9]{7}$",
    "IT_CF_CD": "^[0-9]{11}$",
    "IT_UCITS_CD": "^[0-9]{1,7}$",
    "JP_CN_CD": "^[1-9][0-9]{12}$",
    "LT_INV_CD": "(^[A-Z]{1}[0-9]{3}$)|(^SF[0-9]{3}$)|(^[A-Z]{3}-[0-9]{2}/[0-9]{2}$)|(^[A-Z]{3}-[A-Z]{4}$)",
    "LT_JAR_CD": "^[0-9]{9}$",
    "LU_RCS_CD": "^[A-Z][0-9]+$",
    "LU_VAT_CD": "^[0-9]{8}$",
    "LU_IF_CD": "^[A-Z][0-9]{6}C[0-9]{5}$",
    "LU_NOTAP_CD": "^[^+,]{1,50}$",
    "LV_FON_CD": "(^LVAF[0-9]{3}[AB0-9]{1}[0-9]{2}$)|(^LVIF[0-9]{3}[ABCDEF0-9]{1}[0-9]{2}$)|(^LVLB[0-9]{6}$)"
                 "|(^LVVF[0-9]{6}$)|(^LV[0-9]{11}$)",
    "LV_NBR_CD": "^[0-9]{11}$",
    "LV_VAT_CD": "^LV[0-9]{11}$",
    "MC_CIB_CD": "^[0-9]{5}$",
    "MC_NIS_CD": "^[0-9]{2,4}[A-Z][0-9]{5}$",
    "MC_RCI_CD": "^[0-9]{2}[A-Z]{1,3}[0-9]{5}$",
    "MH_NBR_CD": "^[0-9]{4,6}$",
    "MT_CNUM_CD": "^[^+,]{1,50}$",
    "MT_VAT_CD": "^[0-9]{8}$",
    "MT_OLE_CD": "^[^+,]{1,50}$",
    "MX_RFC_CD": "^[A-Z]{3}-[0-9]{6}-[A-Z0-9]{3}$",
    "NL_KVK_CD": "^[0-9]{8}$",
    "NL_RSIN_CD": "^[0-9]{9}$",
    "NO_NBR_CD": "^[0-9]{9}$",
    "PL_KRS_CD": "^[0-9]+$",
    "PL_NIP_CD": "^[0-9]{10}$",
    "PL_REGON_CD": "(^[0-9]{9}$)|(^[0-9]{14}$)",
    "PL_VAT_CD": "^PL[0-9]{10}$",
    "PT_FSA_CD": "^[0-9]{1,6}$",
    "PT_NIF_CD": "^[0-9]{9}$",
    "RO_CUI_CD": "^RO[0-9]{1,10}$",
    "RO_TAX_CD": "^RO[0-9]{1,10}$",
    "RO_TRN_CD": "^J[0-9]{2}/[0-9]{1,9}/[12][0-9]{3}$",
    "RU_INN_CD": "^[0-9]{10}$",
    "RU_OGRN_CD": "^[0-9]{13}$",
    "SE_FIN_CD": "^[0-9]{5}$",
    "SE_ORG_CD": "^[0-9]{2}[2-9][0-9]{3}-?[0-9]{4}$",
    "SE_MOM_CD": "^SE[0-9]{12}$",
    "SI_DAV_CD": "^[0-9]{8}$",
    "SI_DDV_CD": "^SI[0-9]{8}$",
    "SI_MAT_CD": "^[0-9]{10}$",
    "SK_ICO_CD": "^[0-9]{8}$",
    "SK_IF_CD": "^SK[0-9]{8}[A-Z]{3}[0-9]{2}$",
    "TR_VKN_CD": "^[0-9]{1,10}$",
    "US_EIN_CD": "^[0-9]{2}-[0-9]{7}$",
    "US_DSFN_CD": "^[0-9]{7}$",
    "US_CIK_CD": "^[0-9]{10}$",
}

# List of other identifiers issued by Narodná banka Slovenska
NBS_IDENTIFIERS = {
    "ICO_NI": "^[0-9]{8}[a-z]{1}$",  # IČO NI is issued by NBS for subjects with duplicate national identifier (IČO).
    "NIC": "^[0-9]{8}N[0-9]{6}$",  # NIČ is issued by NBS for foreign (non SK) subjects.
}

IDENTIFIER_FORMATS = {**ECB_NATIONAL_IDENTIFIERS, **NBS_IDENTIFIERS}


def verify_identifier_format(identifier: str, identifier_type: str, allow_unknown_type: bool = True) -> bool:
    """
    Validate identifier format, based on its type
    """
    if not isinstance(identifier, str) or not isinstance(identifier_type, str):
        result = False
    elif identifier_type in IDENTIFIER_FORMATS:
        result = bool(re.match(IDENTIFIER_FORMATS[identifier_type], identifier))
    elif allow_unknown_type:
        result = bool(re.match("[^+,]{1,50}", identifier))
    else:
        result = False

    return result
