# (C) Copyright 2019 Hewlett Packard Enterprise Development LP.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0.

# Unless required by applicable law. or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"

# A python script for getting a dictionary of switches

import pymongo
from lib.actions import MongoBaseAction


class loadDb(MongoBaseAction):
    def run(self, tasks):

        mydb = self.client["app_db"]
        known = mydb["tasks3par"]

        l1={"name":"rick", "age":61}
        l2={"name":"bob", "age":21}
        l3={"name":"joe", "age":41}
        list_o_things = [l1,l2,l3]

        new_record = {}

        for n in list_o_things:
            myquery = { "name" : n['name'] }
            records = known.find(myquery).count()
            if records == 0:
                new_record['name'] = n['name']
                new_record['age'] = n['age']
                write_record = known.insert_one(new_record)
                new_record={}

            else:
                records='Fail to write mongo record, possible duplicate'
                # write_record = process.insert_one(alarm)
        return (records)
