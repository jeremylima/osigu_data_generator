PROFILES = {
    'QA1': {
        'BASE_URL': 'https://qa.paycodenetwork.com/v1',
        'DATABASE': {
            'HOST': 'paycode-rds-qa.cc25dqlmelik.us-east-1.rds.amazonaws.com',
            'USER': 'paycode',
            'PASSWORD': 'c3a5aa411f857f0b88a98d0aec8c8096',
            'PORT': '5432',
            'DATABASE': 'QA1'
        },
        'ELASTIC_SEARCH': 'http://search-osigu-qa-lthrqafin2oam2zwemgisvw5hi.us-east-1.es.amazonaws.com'
    },
    'QA2': {
        'BASE_URL': 'https://qa2.paycodenetwork.com/v1',
        'DATABASE': {
            'HOST': 'paycode-rds-qa.cc25dqlmelik.us-east-1.rds.amazonaws.com',
            'USER': 'paycode',
            'PASSWORD': 'c3a5aa411f857f0b88a98d0aec8c8096',
            'PORT': '5432',
            'DATABASE': 'QA2'
        },
        'ELASTIC_SEARCH': 'http://search-osigu-qa-2-lvjzupivq2warcqblauqug4n5u.us-east-1.es.amazonaws.com'
    },
    'QA3': {
        'BASE_URL': 'https://qa3.paycodenetwork.com/v1',
        'DATABASE': {
            'HOST': 'paycode-rds-qa.cc25dqlmelik.us-east-1.rds.amazonaws.com',
            'USER': 'paycodeqa3',
            'PASSWORD': 'paycode2016',
            'PORT': '5432',
            'DATABASE': 'QA3'
        },
        'ELASTIC_SEARCH': 'http://search-osigu-qa-3-gkcvu4dd4wg3ujnudcgishkiba.us-east-1.es.amazonaws.com'
    },
    'DEV': {
        'BASE_URL': 'https://dev.paycodenetwork.com/v1',
        'DATABASE': {
            'HOST': 'paycode-rds-dev.cc25dqlmelik.us-east-1.rds.amazonaws.com',
            'USER': 'osiguadmin',
            'PASSWORD': 'paycode2016',
            'PORT': '5432',
            'DATABASE': 'paycode_dev'
        },
        'ELASTIC_SEARCH': 'http://search-osigu-dev-xdvzqdp7eg76z7ripslmhwpt5a.us-east-1.es.amazonaws.com'
    }
}
