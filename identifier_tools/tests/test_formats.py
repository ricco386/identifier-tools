from identifier_tools.formats import verify_identifier_format, verify_national_identifier_country
from identifier_tools.formats_constants import IDENTIFIER_FORMATS
from .utils import BadCodeType


def test_invalid_input_identifier_format_type():
    assert verify_identifier_format(identifier=None, identifier_type=None) is False
    assert verify_identifier_format(identifier='12345678', identifier_type=None) is False
    assert verify_identifier_format(identifier=None, identifier_type='SK_ICO_CD') is False
    assert verify_identifier_format(identifier='12345678', identifier_type='SK_ICO_CD') is True

    identifiers = ("11841036", "11841036x")
    identifiers_types = ("SK_ICO_CD", "ICO_NI")
    assert verify_identifier_format(identifier=identifiers, identifier_type=identifiers_types) is False

    identifiers = {
        "ico": "11841036",
        "ico_ni": "11841036x",
    }
    identifiers_types = {
        "ico": "SK_ICO_CD",
        "ico_ni": "ICO_NI"
    }
    assert verify_identifier_format(identifier=identifiers, identifier_type=identifiers_types) is False

    identifier = 11841036
    assert verify_identifier_format(identifier=identifier, identifier_type='SK_ICO_CD') is False
    assert verify_identifier_format(identifier='12345678', identifier_type=identifier) is False

    identifier = BadCodeType()
    assert verify_identifier_format(identifier='12345678', identifier_type=identifier) is False


def test_unknown_type_strict_checking():
    assert verify_identifier_format(identifier='', identifier_type='XX_XXX_XX', allow_unknown_type=True) is False
    assert verify_identifier_format(identifier='', identifier_type='XX_XXX_XX', allow_unknown_type=False) is False

    assert verify_identifier_format(identifier=' ', identifier_type='XX_XXX_XX', allow_unknown_type=True) is True
    assert verify_identifier_format(identifier=' ', identifier_type='XX_XXX_XX', allow_unknown_type=False) is False


def test_known_type_identifier_length():
    for code in IDENTIFIER_FORMATS:
        assert verify_identifier_format(identifier="A" * 80, identifier_type=code) is False


def test_verify_identifier_formats():
    # Samples from European Central Bank spreadsheet
    assert verify_identifier_format(identifier="7934858", identifier_type="AT_IDENT_CD") is True
    assert verify_identifier_format(identifier="79063w", identifier_type="AT_FB_CD") is True
    assert verify_identifier_format(identifier="79063w3", identifier_type="AT_FB_CD") is True
    assert verify_identifier_format(identifier="119982w", identifier_type="AT_FB_CD") is True
    assert verify_identifier_format(identifier="881400879", identifier_type="AT_ZVR_CD") is True
    assert verify_identifier_format(identifier="40801", identifier_type="AT_GEM_CD") is True
    assert verify_identifier_format(identifier="4", identifier_type="AT_LAE_CD") is True
    assert verify_identifier_format(identifier="0203201340", identifier_type="BE_OND_CD") is True
    assert verify_identifier_format(identifier="999999999", identifier_type="BG_UIC_CD") is True
    assert verify_identifier_format(identifier="9999999999999", identifier_type="BG_UIC_CD") is True
    assert verify_identifier_format(identifier="999999999", identifier_type="BG_BULSTAT_CD") is True
    assert verify_identifier_format(identifier="9999999999", identifier_type="BG_BULSTAT_CD") is True
    assert verify_identifier_format(identifier="9999999999999", identifier_type="BG_BULSTAT_CD") is True
    assert verify_identifier_format(identifier="BG999999999", identifier_type="BG_VAT_CD") is True
    assert verify_identifier_format(identifier="BG9999999999", identifier_type="BG_VAT_CD") is True
    assert verify_identifier_format(identifier="05937759187", identifier_type="HR_OIB_CD") is True
    assert verify_identifier_format(identifier="03449602", identifier_type="HR_MB_CD") is True
    assert verify_identifier_format(identifier="080020970", identifier_type="HR_MBS_CD") is True
    assert verify_identifier_format(identifier="CH02030039709", identifier_type="CH_ID_CD") is True
    assert verify_identifier_format(identifier="CH-130.3.018.934-7", identifier_type="CH_NUMMER") is True
    assert verify_identifier_format(identifier="C273730", identifier_type="CY_DRCOR_CD") is True
    assert verify_identifier_format(identifier="DD447", identifier_type="CY_CBCID_CD") is True
    assert verify_identifier_format(identifier="DD447ASASASXCX44", identifier_type="CY_OTHER_CD") is True
    assert verify_identifier_format(identifier="10145530D", identifier_type="CY_VAT_CD") is True
    assert verify_identifier_format(identifier="12000018M", identifier_type="CY_TIC_CD") is True
    assert verify_identifier_format(identifier="CYIF0242", identifier_type="CY_IF_CD") is True
    assert verify_identifier_format(identifier="PF602", identifier_type="CY_PF_CD") is True
    assert verify_identifier_format(identifier="PF3268", identifier_type="CY_PF_CD") is True
    assert verify_identifier_format(identifier="S1311020700", identifier_type="CY_GG_CD") is True
    assert verify_identifier_format(identifier="00006947", identifier_type="CZ_ICO_CD") is True
    assert verify_identifier_format(identifier="90091883", identifier_type="CZ_NID_CD") is True
    assert verify_identifier_format(identifier="8080107948", identifier_type="CZ_NID_CD") is True
    assert verify_identifier_format(identifier="22756214", identifier_type="DK_CVR_CD") is True
    assert verify_identifier_format(identifier="3000-01", identifier_type="DK_FT_CD") is True
    assert verify_identifier_format(identifier="3000", identifier_type="DK_FT_CD") is True
    assert verify_identifier_format(identifier="12345-678", identifier_type="DK_FT_CD") is True
    assert verify_identifier_format(identifier="3-123", identifier_type="DK_FT_CD") is True
    assert verify_identifier_format(identifier="3", identifier_type="DK_FT_CD") is True
    assert verify_identifier_format(identifier="22756214", identifier_type="DK_SE_CD") is True
    assert verify_identifier_format(identifier="10005211", identifier_type="EE_RG_CD") is True
    assert verify_identifier_format(identifier="21", identifier_type="EE_FON_CD") is True
    assert verify_identifier_format(identifier="0112038-9", identifier_type="FI_Y_CD") is True
    assert verify_identifier_format(identifier="01120389", identifier_type="FI_Y_CD") is True
    assert verify_identifier_format(identifier="FI01120389", identifier_type="FI_ALV_CD") is True
    assert verify_identifier_format(identifier="06716026#001", identifier_type="FI_SIRA_CD") is True
    assert verify_identifier_format(identifier="542051180", identifier_type="FR_SIREN_CD") is True
    assert verify_identifier_format(identifier="W861001547", identifier_type="FR_RNA_CD") is True
    assert verify_identifier_format(identifier="30003", identifier_type="FR_CIB") is True
    assert verify_identifier_format(identifier="FR44444AA800", identifier_type="FR_IF_CD") is True
    assert verify_identifier_format(identifier="FR0000000439", identifier_type="FR_IF_CD") is True
    assert verify_identifier_format(identifier="FRPI00004289", identifier_type="FR_IF_CD") is True
    assert verify_identifier_format(identifier="HRA100484-K1101", identifier_type="DE_HRA_CD") is True
    assert verify_identifier_format(identifier="HRB1234-R1101", identifier_type="DE_HRB_CD") is True
    assert verify_identifier_format(identifier="PR2359-Y1101", identifier_type="DE_PR_CD") is True
    assert verify_identifier_format(identifier="GNR3034LA-D4102", identifier_type="DE_GNR_CD") is True
    assert verify_identifier_format(identifier="GnR3034LA-D4102", identifier_type="DE_GNR_CD") is True
    assert verify_identifier_format(identifier="VR350378-M1305", identifier_type="DE_VR_CD") is True
    assert verify_identifier_format(identifier="940498654", identifier_type="GR_AFM_CD") is True
    assert verify_identifier_format(identifier="GB412051121", identifier_type="GB_VAT_CD") is True
    assert verify_identifier_format(identifier="GB532476983177", identifier_type="GB_VAT_CD") is True
    assert verify_identifier_format(identifier="GBGD321", identifier_type="GB_VAT_CD") is True
    assert verify_identifier_format(identifier="GBHA666", identifier_type="GB_VAT_CD") is True
    assert verify_identifier_format(identifier="827161", identifier_type="GB_FSR_CD") is True
    assert verify_identifier_format(identifier="9074729", identifier_type="GR_IMO_CD") is True
    assert verify_identifier_format(identifier="99999999", identifier_type="HU_TOR_CD") is True
    assert verify_identifier_format(identifier="FB999999", identifier_type="HU_FB_CD") is True
    assert verify_identifier_format(identifier="FB999A99", identifier_type="HU_FB_CD") is True
    assert verify_identifier_format(identifier="HU99999999", identifier_type="HU_KOZ_CD") is True
    assert verify_identifier_format(identifier="01-17-000705", identifier_type="HU_CEG_CD") is True
    assert verify_identifier_format(identifier="900488", identifier_type="IE_CRO_CD") is True
    assert verify_identifier_format(identifier="00470400011", identifier_type="IT_CF_CD") is True
    assert verify_identifier_format(identifier="NA0091712", identifier_type="IT_CCIAA_CD") is True
    assert verify_identifier_format(identifier="103900", identifier_type="IT_UCITS_CD") is True
    assert verify_identifier_format(identifier="40103681895", identifier_type="LV_NBR_CD") is True
    assert verify_identifier_format(identifier="LV40103681895", identifier_type="LV_VAT_CD") is True
    assert verify_identifier_format(identifier="LVIF263002", identifier_type="LV_FON_CD") is True
    assert verify_identifier_format(identifier="LVIF098D10", identifier_type="LV_FON_CD") is True
    assert verify_identifier_format(identifier="LVAF098101", identifier_type="LV_FON_CD") is True
    assert verify_identifier_format(identifier="LVAF211B02", identifier_type="LV_FON_CD") is True
    assert verify_identifier_format(identifier="LV44103104436", identifier_type="LV_FON_CD") is True
    assert verify_identifier_format(identifier="LV40203123846", identifier_type="LV_FON_CD") is True
    assert verify_identifier_format(identifier="LVB001007", identifier_type="LV_FON_CD") is True
    assert verify_identifier_format(identifier="LVVF098010", identifier_type="LV_FON_CD") is True
    assert verify_identifier_format(identifier="110486217", identifier_type="LT_JAR_CD") is True
    assert verify_identifier_format(identifier="F001", identifier_type="LT_INV_CD") is True
    assert verify_identifier_format(identifier="I001", identifier_type="LT_INV_CD") is True
    assert verify_identifier_format(identifier="P001", identifier_type="LT_INV_CD") is True
    assert verify_identifier_format(identifier="V001", identifier_type="LT_INV_CD") is True
    assert verify_identifier_format(identifier="D001", identifier_type="LT_INV_CD") is True
    assert verify_identifier_format(identifier="S001", identifier_type="LT_INV_CD") is True
    assert verify_identifier_format(identifier="SF007", identifier_type="LT_INV_CD") is True
    assert verify_identifier_format(identifier="SF123", identifier_type="LT_INV_CD") is True
    assert verify_identifier_format(identifier="AVI-68/74", identifier_type="LT_INV_CD") is True
    assert verify_identifier_format(identifier="INV-TIPF", identifier_type="LT_INV_CD") is True
    assert verify_identifier_format(identifier="B0030775", identifier_type="LU_RCS_CD") is True
    assert verify_identifier_format(identifier="C126", identifier_type="LU_RCS_CD") is True
    assert verify_identifier_format(identifier="10355144", identifier_type="LU_VAT_CD") is True
    assert verify_identifier_format(identifier="O123456C12345", identifier_type="LU_IF_CD") is True
    assert verify_identifier_format(identifier="8232", identifier_type="MH_NBR_CD") is True
    assert verify_identifier_format(identifier="53765", identifier_type="MH_NBR_CD") is True
    assert verify_identifier_format(identifier="478893", identifier_type="MH_NBR_CD") is True
    assert verify_identifier_format(identifier="13240110", identifier_type="MT_VAT_CD") is True
    assert verify_identifier_format(identifier="C 12345", identifier_type="MT_CNUM_CD") is True
    assert verify_identifier_format(identifier="VO/0467", identifier_type="MT_OLE_CD") is True
    assert verify_identifier_format(identifier="30003", identifier_type="MC_CIB") is True
    assert verify_identifier_format(identifier="84P02123", identifier_type="MC_RCI_CD") is True
    assert verify_identifier_format(identifier="84S02071", identifier_type="MC_RCI_CD") is True
    assert verify_identifier_format(identifier="6110Z07638", identifier_type="MC_NIS_CD") is True
    assert verify_identifier_format(identifier="6110Z07638", identifier_type="MC_NIS_CD") is True
    assert verify_identifier_format(identifier="12345678", identifier_type="NL_KVK_CD") is True
    assert verify_identifier_format(identifier="123456789", identifier_type="NL_RSIN_CD") is True
    assert verify_identifier_format(identifier="610188201", identifier_type="PL_REGON_CD") is True
    assert verify_identifier_format(identifier="56228", identifier_type="PL_KRS_CD") is True
    assert verify_identifier_format(identifier="7740001454", identifier_type="PL_NIP_CD") is True
    assert verify_identifier_format(identifier="PL7740001454", identifier_type="PL_VAT_CD") is True
    assert verify_identifier_format(identifier="500792771", identifier_type="PT_NIF_CD") is True
    assert verify_identifier_format(identifier="502", identifier_type="PT_FSA_CD") is True
    assert verify_identifier_format(identifier="RO1234567890", identifier_type="RO_CUI_CD") is True
    assert verify_identifier_format(identifier="J40/8302/1997", identifier_type="RO_TRN_CD") is True
    assert verify_identifier_format(identifier="RO9999999999", identifier_type="RO_TAX_CD") is True
    assert verify_identifier_format(identifier="31364501", identifier_type="SK_ICO_CD") is True
    assert verify_identifier_format(identifier="SK35742968TAM24", identifier_type="SK_IF_CD") is True
    assert verify_identifier_format(identifier="5063345000", identifier_type="SI_MAT_CD") is True
    assert verify_identifier_format(identifier="79007589", identifier_type="SI_DAV_CD") is True
    assert verify_identifier_format(identifier="SI79007589", identifier_type="SI_DDV_CD") is True
    assert verify_identifier_format(identifier="A28015865", identifier_type="ES_NIF_CD") is True
    assert verify_identifier_format(identifier="S2826011E", identifier_type="ES_NIF_CD") is True
    assert verify_identifier_format(identifier="554521-5795", identifier_type="SE_ORG_CD") is True
    assert verify_identifier_format(identifier="5545215795", identifier_type="SE_ORG_CD") is True
    assert verify_identifier_format(identifier="11187", identifier_type="SE_FIN_CD") is True
    assert verify_identifier_format(identifier="SE554521579501", identifier_type="SE_MOM_CD") is True
    assert verify_identifier_format(identifier="1111", identifier_type="GEN_VAT_CD") is True
    assert verify_identifier_format(identifier="1111", identifier_type="GEN_TAX_CD") is True
    assert verify_identifier_format(identifier="1111", identifier_type="GEN_NBR_ENTTY_CD") is True
    assert verify_identifier_format(identifier="1111", identifier_type="GEN_TRD_RGSTR_ENTTY_CD") is True
    assert verify_identifier_format(identifier="1111", identifier_type="GEN_NSI_ENTTY_CD") is True
    assert verify_identifier_format(identifier="1111", identifier_type="GEN_NCB_ENTTY_CD") is True
    assert verify_identifier_format(identifier="1111", identifier_type="GEN_NSA_ENTTY_CD") is True
    assert verify_identifier_format(identifier="1111", identifier_type="GEN_PS_CD") is True
    assert verify_identifier_format(identifier="1111", identifier_type="GEN_IPF_CD") is True
    assert verify_identifier_format(identifier="1111", identifier_type="GEN_OTHER_CD") is True
    assert verify_identifier_format(identifier="BNPAFRPPXXX", identifier_type="BIC") is True
    assert verify_identifier_format(identifier="BNPAFRPP", identifier_type="BIC") is True
    assert verify_identifier_format(identifier="21.325.097/2156-88", identifier_type="BR_CNPJ_CD") is True
    assert verify_identifier_format(identifier="167251986", identifier_type="CA_BN_CD") is True
    assert verify_identifier_format(identifier="CHE-123.456.789", identifier_type="CH_UID_CD") is True
    assert verify_identifier_format(identifier="167251986167251433", identifier_type="CN_CC_CD") is True
    assert verify_identifier_format(identifier="01234567", identifier_type="GB_CRN_CD") is True
    assert verify_identifier_format(identifier="SC012345", identifier_type="GB_CRN_CD") is True
    assert verify_identifier_format(identifier="NL012345", identifier_type="GB_CRN_CD") is True
    assert verify_identifier_format(identifier="2415326715", identifier_type="GB_UTR_CD") is True
    assert verify_identifier_format(identifier="241532671K", identifier_type="GB_UTR_CD") is True
    assert verify_identifier_format(identifier="L28920MH1945PLC004520", identifier_type="IN_CIN_CD") is True
    assert verify_identifier_format(identifier="AFZPK7190K", identifier_type="IN_PAN_CD") is True
    assert verify_identifier_format(identifier="1251425368993", identifier_type="JP_CN_CD") is True
    assert verify_identifier_format(identifier="GFI-920961-IL7", identifier_type="MX_RFC_CD") is True
    assert verify_identifier_format(identifier="1624351625", identifier_type="RU_INN_CD") is True
    assert verify_identifier_format(identifier="1036165026589", identifier_type="RU_OGRN_CD") is True
    assert verify_identifier_format(identifier="71524152", identifier_type="TR_VKN_CD") is True
    assert verify_identifier_format(identifier="21-2567152", identifier_type="US_EIN_CD") is True
    assert verify_identifier_format(identifier="2153177", identifier_type="HK_CR_CD") is True
    assert verify_identifier_format(identifier="GV1040", identifier_type="IE_GOV_CD") is True
    assert verify_identifier_format(identifier="LA006", identifier_type="IE_GOV_CD") is True
    assert verify_identifier_format(identifier="987654321", identifier_type="NO_NBR_CD") is True
    assert verify_identifier_format(identifier="4307493", identifier_type="US_DSFN_CD") is True
    assert verify_identifier_format(identifier="0001543040", identifier_type="US_CIK_CD") is True
    assert verify_identifier_format(identifier="123-to-je-jedno-nema-regex", identifier_type="GEN_NOTAP_CD") is True
    assert verify_identifier_format(identifier="123-to-je-jedno-nema-regex", identifier_type="AT_NOTAP_CD") is True
    assert verify_identifier_format(identifier="123-to-je-jedno-nema-regex", identifier_type="SE_NOTAP_CD") is True
    assert verify_identifier_format(identifier="123-to-je-jedno-nema-regex", identifier_type="IE_NOTAP_CD") is True


def test_invalid_identifier_formats():
    # Edge cases in regex which shouldnt pass
    assert verify_identifier_format(identifier="31364501a", identifier_type="SK_ICO_CD") is False
    assert verify_identifier_format(identifier="551521-5795", identifier_type="SE_ORG_CD") is False
    assert verify_identifier_format(identifier="5505215795", identifier_type="SE_ORG_CD") is False


def test_verify_national_identifier_country_true():
    assert verify_national_identifier_country(country_code="CZ", national_id_type="CZ_ICO_CD") is True
    assert verify_national_identifier_country(country_code="ZZ", national_id_type="BIC") is True
    assert verify_national_identifier_country(country_code="ZZ", national_id_type="GEN_OTHER_CD") is True

    # Territory mapper case
    assert verify_national_identifier_country(country_code="BL", national_id_type="FR_RNA_CD") is True

    # Monaco special case
    assert verify_national_identifier_country(country_code="MC", national_id_type="MC_CIB") is True

    # Check countries from GEN_IDENTIFIER_COUNTRY_EXCEPTIONS
    assert verify_national_identifier_country(country_code="BR", national_id_type="GEN_OTHER_CD") is True
    assert verify_national_identifier_country(country_code="CA", national_id_type="GEN_OTHER_CD") is True
    assert verify_national_identifier_country(country_code="CH", national_id_type="GEN_OTHER_CD") is True
    assert verify_national_identifier_country(country_code="CN", national_id_type="GEN_OTHER_CD") is True
    assert verify_national_identifier_country(country_code="GB", national_id_type="GEN_OTHER_CD") is True
    assert verify_national_identifier_country(country_code="HK", national_id_type="GEN_OTHER_CD") is True
    assert verify_national_identifier_country(country_code="IN", national_id_type="GEN_OTHER_CD") is True
    assert verify_national_identifier_country(country_code="JP", national_id_type="GEN_OTHER_CD") is True
    assert verify_national_identifier_country(country_code="MX", national_id_type="GEN_OTHER_CD") is True
    assert verify_national_identifier_country(country_code="RU", national_id_type="GEN_OTHER_CD") is True
    assert verify_national_identifier_country(country_code="TR", national_id_type="GEN_OTHER_CD") is True
    assert verify_national_identifier_country(country_code="US", national_id_type="GEN_OTHER_CD") is True


def test_verify_national_identifier_country_false():
    assert verify_national_identifier_country(country_code="SK", national_id_type="CZ_ICO_CD") is False
    assert verify_national_identifier_country(country_code="ZZ", national_id_type="NON_EXISTING_TYPE") is False
