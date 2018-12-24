# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from apiron.service.base import Service
from apiron.endpoint import JsonEndpoint, StreamingEndpoint, Endpoint
from apiron.client import ServiceCaller

__all__=['BaseService', 'BaseCaller']

class BaseService(Service):
    def __init__(self, domain, *args, **kwargs):
        self.domain = domain if domain.endswith('/') else '/'.join((domain, ''))
        super(*args, **kwargs)

    find = JsonEndpoint(path='tools/find', default_method=['POST'])

class BaseCaller:
    def __init__(self):
        raise NotImplemented

    def find(self, query, **kwargs):
        return ServiceCaller(self.service, self.service.find, data=query, **kwargs)