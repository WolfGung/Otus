import pytest


@pytest.fixture()
def url_list_suite_1():
    # url links
    list_all_breed_request = "https://dog.ceo/api/breeds/list/all"
    random_request = "https://dog.ceo/api/breeds/image/random"
    multiple_random_request = "https://dog.ceo/api/breeds/image/random/3"
    hound_image_request = "https://dog.ceo/api/breed/hound/images"
    random_breed_request = "https://dog.ceo/api/breed/hound/images/random"
    random_multiple_breed_request = "https://dog.ceo/api/breed/hound/images/random/3"
    list_sub_breed_request = "https://dog.ceo/api/breed/hound/list"
    hound_afghan_request = "https://dog.ceo/api/breed/hound/afghan/images"
    random_afghan_image_request = "https://dog.ceo/api/breed/hound/afghan/images/random"
    random_multiple_afghan_image_request = "https://dog.ceo/api/breed/hound/afghan/images/random/3"
    # url links list
    url_list = (list_all_breed_request, random_request, multiple_random_request, hound_image_request,
                random_breed_request, random_multiple_breed_request, list_sub_breed_request,
                hound_afghan_request, random_afghan_image_request, random_multiple_afghan_image_request)
    return url_list


@pytest.fixture()
def url_list_suite_2():
    # url links
    breweries = "https://api.openbrewerydb.org/breweries"
    breweries_by_state = "https://api.openbrewerydb.org/breweries?by_state=new_york"
    breweries_by_name = "https://api.openbrewerydb.org/breweries?by_name=cooper"
    breweries_by_tag = "https://api.openbrewerydb.org/breweries?by_tag=patio"
    breweries_by_name_and_state = "https://api.openbrewerydb.org/breweries?by_name=cooper&by_state=new_york"
    breweries_by_state_type_name = "https://api.openbrewerydb.org/breweries?by_state=ohio&sort=type,-name"
    breweries_pagination = "https://api.openbrewerydb.org/breweries?page=2&per_page=30"
    get_one_brewery = "https://api.openbrewerydb.org/breweries/5494"
    brewery_autocomplete = "https://api.openbrewerydb.org/breweries/autocomplete?query=dog"
    brewery_search = "https://api.openbrewerydb.org/breweries/search?query=dog"
    # url links list
    url_list = (breweries, breweries_by_state, breweries_by_name, breweries_by_tag,
                breweries_by_name_and_state, breweries_by_state_type_name, breweries_pagination,
                get_one_brewery, brewery_autocomplete, brewery_search)
    return url_list


@pytest.fixture()
def url_list_suite_3():
    # url links
    cdnjs_wo_parameters = "https://api.cdnjs.com/libraries"
    cdnjs_search = "https://api.cdnjs.com/libraries?search=[query]"
    cdnjs_name_search = "https://api.cdnjs.com/libraries/[name]"
    cdnjs_with_parameters = "https://api.cdnjs.com/libraries/jquery?fields=name,filename,version"
    cdnjs_human_readable = "https://api.cdnjs.com/libraries?output=human"
    cdnjs_more_data = "https://api.cdnjs.com/libraries?search=[query]&fields=version,description"
    cdnjs_library_list = "https://api.cdnjs.com/libraries?search=[query]&fields=assets"
    cdnjs_jquery_library = "https://api.cdnjs.com/libraries/jquery"
    cdnjs_ractive_search = "https://api.cdnjs.com/libraries?search=ractive"
    cdnjs_human_readable_jquery = "https://api.cdnjs.com/libraries?search=jquery&output=human"
    cdnjs_specific_field_search = "https://api.cdnjs.com/libraries?search=ractive&fields=version,description"
    cdnjs_specific_library_assets = "https://api.cdnjs.com/libraries?search=1140&fields=assets"
    cdnjs_specific_hr_assets = "https://api.cdnjs.com/libraries?search=1140&fields=assets&output=human"
    # url link list
    url_list = (cdnjs_wo_parameters, cdnjs_search, cdnjs_name_search, cdnjs_with_parameters, cdnjs_human_readable,
                cdnjs_more_data, cdnjs_library_list, cdnjs_jquery_library, cdnjs_ractive_search,
                cdnjs_human_readable_jquery, cdnjs_specific_field_search, cdnjs_specific_library_assets,
                cdnjs_specific_hr_assets)
    return url_list
