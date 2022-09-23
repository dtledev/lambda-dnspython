import json
import dns.resolver
import os

def lambda_handler(event, context):
    '''Lambda handler'''
    # domain in domain env var
    domain = os.environ['domain']
    A = dns.resolver.resolve(domain, 'A')

    # Print all domains returned
    for answer in A.response.answer:
        for item in answer.items:
            print(item.address)
    
    # # Get current DNS server
    # dns_resolver = dns.resolver.Resolver()
    # print(dns_resolver.nameservers[0])
    
    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }
