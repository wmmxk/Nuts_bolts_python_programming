from chembl_webresource_client.new_client import new_client
from chembl_webresource_client.target_resource import TargetResource


def test_find_ki():

    targets = TargetResource()
    print(targets.get(['CHEMBL240', 'CHEMBL1927']))
