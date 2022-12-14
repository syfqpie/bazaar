from django.db import models


class CountryChoice(models.TextChoices):
    """
    Integer choices for countries
    """

    AD = 'AD', 'Andorra'
    AE = 'AE', 'United Arab Emirates'
    AF = 'AF', 'Afghanistan'
    AG = 'AG', 'Antigua & Barbuda'
    AI = 'AI', 'Anguilla'
    AL = 'AL', 'Albania'
    AM = 'AM', 'Armenia'
    AN = 'AN', 'Netherlands Antilles'
    AO = 'AO', 'Angola'
    AQ = 'AQ', 'Antarctica'
    AR = 'AR', 'Argentina'
    AS = 'AS', 'American Samoa'
    AT = 'AT', 'Austria'
    AU = 'AU', 'Australia'
    AW = 'AW', 'Aruba'
    AZ = 'AZ', 'Azerbaijan'
    BA = 'BA', 'Bosnia and Herzegovina'
    BB = 'BB', 'Barbados'
    BD = 'BD', 'Bangladesh'
    BE = 'BE', 'Belgium'
    BF = 'BF', 'Burkina Faso'
    BG = 'BG', 'Bulgaria'
    BH = 'BH', 'Bahrain'
    BI = 'BI', 'Burundi'
    BJ = 'BJ', 'Benin'
    BM = 'BM', 'Bermuda'
    BN = 'BN', 'Brunei Darussalam'
    BO = 'BO', 'Bolivia'
    BR = 'BR', 'Brazil'
    BS = 'BS', 'Bahama'
    BT = 'BT', 'Bhutan'
    BU = 'BU', 'Burma (no longer exists)'
    BV = 'BV', 'Bouvet Island'
    BW = 'BW', 'Botswana'
    BY = 'BY', 'Belarus'
    BZ = 'BZ', 'Belize'
    CA = 'CA', 'Canada'
    CC = 'CC', 'Cocos (Keeling) Islands'
    CF = 'CF', 'Central African Republic'
    CG = 'CG', 'Congo'
    CH = 'CH', 'Switzerland'
    CI = 'CI', 'Côte D\'ivoire (Ivory Coast)'
    CK = 'CK', 'Cook Iislands'
    CL = 'CL', 'Chile'
    CM = 'CM', 'Cameroon'
    CN = 'CN', 'China'
    CO = 'CO', 'Colombia'
    CR = 'CR', 'Costa Rica'
    CS = 'CS', 'Czechoslovakia (no longer exists)'
    CU = 'CU', 'Cuba'
    CV = 'CV', 'Cape Verde'
    CX = 'CX', 'Christmas Island'
    CY = 'CY', 'Cyprus'
    CZ = 'CZ', 'Czech Republic'
    DD = 'DD', 'German Democratic Republic (no longer exists)'
    DE = 'DE', 'Germany'
    DJ = 'DJ', 'Djibouti'
    DK = 'DK', 'Denmark'
    DM = 'DM', 'Dominica'
    DO = 'DO', 'Dominican Republic'
    DZ = 'DZ', 'Algeria'
    EC = 'EC', 'Ecuador'
    EE = 'EE', 'Estonia'
    EG = 'EG', 'Egypt'
    EH = 'EH', 'Western Sahara'
    ER = 'ER', 'Eritrea'
    ES = 'ES', 'Spain'
    ET = 'ET', 'Ethiopia'
    FI = 'FI', 'Finland'
    FJ = 'FJ', 'Fiji'
    FK = 'FK', 'Falkland Islands (Malvinas)'
    FM = 'FM', 'Micronesia'
    FO = 'FO', 'Faroe Islands'
    FR = 'FR', 'France'
    FX = 'FX', 'France, Metropolitan'
    GA = 'GA', 'Gabon'
    GB = 'GB', 'United Kingdom (Great Britain)'
    GD = 'GD', 'Grenada'
    GE = 'GE', 'Georgia'
    GF = 'GF', 'French Guiana'
    GH = 'GH', 'Ghana'
    GI = 'GI', 'Gibraltar'
    GL = 'GL', 'Greenland'
    GM = 'GM', 'Gambia'
    GN = 'GN', 'Guinea'
    GP = 'GP', 'Guadeloupe'
    GQ = 'GQ', 'Equatorial Guinea'
    GR = 'GR', 'Greece'
    GS = 'GS', 'South Georgia and the South Sandwich Islands'
    GT = 'GT', 'Guatemala'
    GU = 'GU', 'Guam'
    GW = 'GW', 'Guinea-Bissau'
    GY = 'GY', 'Guyana'
    HK = 'HK', 'Hong Kong'
    HM = 'HM', 'Heard & McDonald Islands'
    HN = 'HN', 'Honduras'
    HR = 'HR', 'Croatia'
    HT = 'HT', 'Haiti'
    HU = 'HU', 'Hungary'
    ID = 'ID', 'Indonesia'
    IE = 'IE', 'Ireland'
    IL = 'IL', 'Israel'
    IN = 'IN', 'India'
    IO = 'IO', 'British Indian Ocean Territory'
    IQ = 'IQ', 'Iraq'
    IR = 'IR', 'Islamic Republic of Iran'
    IS = 'IS', 'Iceland'
    IT = 'IT', 'Italy'
    JM = 'JM', 'Jamaica'
    JO = 'JO', 'Jordan'
    JP = 'JP', 'Japan'
    KE = 'KE', 'Kenya'
    KG = 'KG', 'Kyrgyzstan'
    KH = 'KH', 'Cambodia'
    KI = 'KI', 'Kiribati'
    KM = 'KM', 'Comoros'
    KN = 'KN', 'St. Kitts and Nevis'
    KP = 'KP', 'Korea, Democratic People\'s Republic of'
    KR = 'KR', 'Korea, Republic of'
    KW = 'KW', 'Kuwait'
    KY = 'KY', 'Cayman Islands'
    KZ = 'KZ', 'Kazakhstan'
    LA = 'LA', 'Lao People\'s Democratic Republic'
    LB = 'LB', 'Lebanon'
    LC = 'LC', 'Saint Lucia'
    LI = 'LI', 'Liechtenstein'
    LK = 'LK', 'Sri Lanka'
    LR = 'LR', 'Liberia'
    LS = 'LS', 'Lesotho'
    LT = 'LT', 'Lithuania'
    LU = 'LU', 'Luxembourg'
    LV = 'LV', 'Latvia'
    LY = 'LY', 'Libyan Arab Jamahiriya'
    MA = 'MA', 'Morocco'
    MC = 'MC', 'Monaco'
    MD = 'MD', 'Moldova, Republic of'
    MG = 'MG', 'Madagascar'
    MH = 'MH', 'Marshall Islands'
    ML = 'ML', 'Mali'
    MN = 'MN', 'Mongolia'
    MM = 'MM', 'Myanmar'
    MO = 'MO', 'Macau'
    MP = 'MP', 'Northern Mariana Islands'
    MQ = 'MQ', 'Martinique'
    MR = 'MR', 'Mauritania'
    MS = 'MS', 'Monserrat'
    MT = 'MT', 'Malta'
    MU = 'MU', 'Mauritius'
    MV = 'MV', 'Maldives'
    MW = 'MW', 'Malawi'
    MX = 'MX', 'Mexico'
    MY = 'MY', 'Malaysia'
    MZ = 'MZ', 'Mozambique'
    NA = 'NA', 'Namibia'
    NC = 'NC', 'New Caledonia'
    NE = 'NE', 'Niger'
    NF = 'NF', 'Norfolk Island'
    NG = 'NG', 'Nigeria'
    NI = 'NI', 'Nicaragua'
    NL = 'NL', 'Netherlands'
    NO = 'NO', 'Norway'
    NP = 'NP', 'Nepal'
    NR = 'NR', 'Nauru'
    NT = 'NT', 'Neutral Zone (no longer exists)'
    NU = 'NU', 'Niue'
    NZ = 'NZ', 'New Zealand'
    OM = 'OM', 'Oman'
    PA = 'PA', 'Panama'
    PE = 'PE', 'Peru'
    PF = 'PF', 'French Polynesia'
    PG = 'PG', 'Papua New Guinea'
    PH = 'PH', 'Philippines'
    PK = 'PK', 'Pakistan'
    PL = 'PL', 'Poland'
    PM = 'PM', 'St. Pierre & Miquelon'
    PN = 'PN', 'Pitcairn'
    PR = 'PR', 'Puerto Rico'
    PT = 'PT', 'Portugal'
    PW = 'PW', 'Palau'
    PY = 'PY', 'Paraguay'
    QA = 'QA', 'Qatar'
    RE = 'RE', 'Réunion'
    RO = 'RO', 'Romania'
    RU = 'RU', 'Russian Federation'
    RW = 'RW', 'Rwanda'
    SA = 'SA', 'Saudi Arabia'
    SB = 'SB', 'Solomon Islands'
    SC = 'SC', 'Seychelles'
    SD = 'SD', 'Sudan'
    SE = 'SE', 'Sweden'
    SG = 'SG', 'Singapore'
    SH = 'SH', 'St. Helena'
    SI = 'SI', 'Slovenia'
    SJ = 'SJ', 'Svalbard & Jan Mayen Islands'
    SK = 'SK', 'Slovakia'
    SL = 'SL', 'Sierra Leone'
    SM = 'SM', 'San Marino'
    SN = 'SN', 'Senegal'
    SO = 'SO', 'Somalia'
    SR = 'SR', 'Suriname'
    ST = 'ST', 'Sao Tome & Principe'
    SU = 'SU', 'Union of Soviet Socialist Republics (no longer exists)'
    SV = 'SV', 'El Salvador'
    SY = 'SY', 'Syrian Arab Republic'
    SZ = 'SZ', 'Swaziland'
    TC = 'TC', 'Turks & Caicos Islands'
    TD = 'TD', 'Chad'
    TF = 'TF', 'French Southern Territories'
    TG = 'TG', 'Togo'
    TH = 'TH', 'Thailand'
    TJ = 'TJ', 'Tajikistan'
    TK = 'TK', 'Tokelau'
    TM = 'TM', 'Turkmenistan'
    TN = 'TN', 'Tunisia'
    TO = 'TO', 'Tonga'
    TP = 'TP', 'East Timor'
    TR = 'TR', 'Turkey'
    TT = 'TT', 'Trinidad & Tobago'
    TV = 'TV', 'Tuvalu'
    TW = 'TW', 'Taiwan, Province of China'
    TZ = 'TZ', 'Tanzania, United Republic of'
    UA = 'UA', 'Ukraine'
    UG = 'UG', 'Uganda'
    UM = 'UM', 'United States Minor Outlying Islands'
    US = 'US', 'United States of America'
    UY = 'UY', 'Uruguay'
    UZ = 'UZ', 'Uzbekistan'
    VA = 'VA', 'Vatican City State (Holy See)'
    VC = 'VC', 'St. Vincent & the Grenadines'
    VE = 'VE', 'Venezuela'
    VG = 'VG', 'British Virgin Islands'
    VI = 'VI', 'United States Virgin Islands'
    VN = 'VN', 'Viet Nam'
    VU = 'VU', 'Vanuatu'
    WF = 'WF', 'Wallis & Futuna Islands'
    WS = 'WS', 'Samoa'
    YD = 'YD', 'Democratic Yemen (no longer exists)'
    YE = 'YE', 'Yemen'
    YT = 'YT', 'Mayotte'
    YU = 'YU', 'Yugoslavia'
    ZA = 'ZA', 'South Africa'
    ZM = 'ZM', 'Zambia'
    ZR = 'ZR', 'Zaire'
    ZW = 'ZW', 'Zimbabwe'
    ZZ = 'ZZ', 'Unknown or unspecified country'
