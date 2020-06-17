
import urllib

from OSMPythonTools.overpass import Overpass


class CustomOverpass(Overpass):
    
    # make sure it is GET method with properly (from the point of overpass api server) 
    # escaped query strings
    def _queryRequest(self, endpoint, queryString, params=None):
        # is the the overpass server broken?
        # qstr = urllib.parse.urlencode({'data': queryString, **(params or {})})
        qstr = "&".join(f"{k}={v}" for k, v in {'data': queryString, **(params or {})}.items())
        print( endpoint + f"interpreter?{qstr}")
        return urllib.request.Request(
            endpoint + f"interpreter?{qstr}", 
            method="GET"
        )
    
    # add util method for building sample queries
    def from_statements(self, statements, **kwargs):
        query = (
            "(" + 
            ";".join(statement for statement in statements) +
            ";);" +
            "out+skel+body+meta+geom;"
        )
        
        return self.query(query, **kwargs)
